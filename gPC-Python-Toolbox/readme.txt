This Python toolbox is developed by the Aerospace Systems Laboratory, The University of Texas at Arlington. 

Language: Python

This toolbox carries out uncertainty quantification and propagation using pseudospectral collocation-based gPC
expansion. The nodes and weights are calculated using the mixed sparse grid quadrature technique. For any stochastic process, this toolbox 
can calculate mean, variance and covariance.

Note: This toolbox is applicable for uncertainties with Gaussian and Uniform distribution.


+-----------------------------------------------------------------------------------------------------------
| Installation
+-----------------------------------------------------------------------------------------------------------
	
	1) Clone this GitHub repository.
	2) Create main_module.py and ode.py as required.
	Note: Users can edit the sample_main_module.py and sample_ode.py provided in the toolbox for convenience. 
	3) Copy main_module.py, ode.py, and all other modules in the repository to the same folder.
	4) Run main_module.py.
	
	
+-----------------------------------------------------------------------------------------------------------
| Creating Main Module and ODE Module.

	Create the Main module as required (For user convenience sample Main modules are provided with this toolbox.)
 
+-----------------------------------------------------------------------------------------------------------

+-----------------------------------------------------------------------------------------------------------
| Sample Main Module 1

	For uncertainty quantification in the Mass Spring Damper system
 
+-----------------------------------------------------------------------------------------------------------
###############################################################################
### This is the sample main_module for uncertainty quantification in Mass Spring
### Damper System.
###############################################################################

###############################################################################
## Importing necessary functions
###############################################################################

from gpc_essentials import gpc_essentials
from gpc_covariance import gpc_covariance
from gpc_coefficients_cal import gpc_coefficients_cal
from msg_quadrature import msg_quadrature
from gaussian_transformation import gaussian_transformation
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from ode import ode
import math
import numpy as np

###############################################################################
## Class definition
###############################################################################

class MSG:
   
    P = 3               # Polynomial Chaos Order
    d = 2               # Dimensions of uncertain variables
    d_Gaussian = 2      # Number of Gaussian random variables
    d_Uniform = 0       # Number of Uniform random variable
    L = 6               # Maximum accuracy level
    
class Parameter:
   
    m = 4               # mass in Kg
    c = 2               # Damping constant in Ns/m
    k = 45              # Spring constant in N/m
  
class Uncertainty:
    # Uncertain Variable with Gaussian Distribution
    
    mu = np.array([4,1])    # Mean vector of initial position (m) 
                            # and initial velocity
    sig = np.array([1,0.1]) # Sigma vector of initial position and 
                            # initial velocity
                            
    # Uncertain Variable with Uniform Distribution
    # Specify a vector of lower bounds of the uniformly distributed 
    # random variables
    
    # lb = np.array([8, 18])  # lower bound of m and c
    
    # Specify a vector of upper bounds of the uniformly distributed random variables
    
    # ub = np.array([12, 22]) # upper bound of m and c


###############################################################################
## Creating Objects
###############################################################################

msg = MSG()
param= Parameter()
uc = Uncertainty()

###############################################################################
## Time vector for integration
###############################################################################

dt = 0.1
tvec = np.arange(0,25+dt,dt)

###############################################################################
## Obtain the nodes and weights from mixed sparse grid quadrature
###############################################################################

[nodes,w] = msg_quadrature(msg)       

Q= max(nodes.shape);   # Total sample size		      

print('==========  Generated MSG Nodes and Weights  ==========')
print('\n');
print(' Number of MSG Nodes generated = %d', Q)

###############################################################################
## Essentials of gPC expansion
###############################################################################

[Norm_psi, N, V_gpc , phi] = gpc_essentials(msg,nodes)   

print('==========  Generated essentials of gPC expansion  ==========');
          

###############################################################################
##Gaussian Affine Transformation
###############################################################################

x_G = gaussian_transformation(uc.mu, uc.sig ,nodes, msg.d_Gaussian)

###############################################################################
## Adjustment for uniformily distributed parameters
###############################################################################

# x_U = uniform_transformation(uc.lb,uc.ub,nodes_sg,msg.d_Gaussian,msg.d_Uniform)


###############################################################################
## Obtain the solution of quantities of interest
###############################################################################

# Buffer
x1 = np.zeros([len(tvec),Q])
x2 = np.zeros([len(tvec),Q])

for cc in range(0,Q):
    
    X0 = [x_G[cc,0],x_G[cc,0]]     # Initial Conditions
    X1 = solve_ivp(ode,[tvec[0],tvec[-1]],X0,method='RK45',t_eval = tvec,\
                   args=(param,),vectorized = True) 
   
    x1[:,cc] = X1.y[0,:]  # First state
    x2[:,cc] = X1.y[1,:]  # Second state 

###############################################################################
## Post processing
###############################################################################
   
# gPC coefficients calculation of propagated collocation points

coeff_x1 = gpc_coefficients_cal(Norm_psi,phi,w,x1)
coeff_x2 = gpc_coefficients_cal(Norm_psi,phi,w,x2)

###################################
# Mean and Variances Calculation
###################################
# Mean 
#########

x1_mean = coeff_x1[0, :]
x2_mean = coeff_x2[0, :]

############################
## Variance and covariances
############################

# Creating Buffer

var_x1=np.zeros(max(tvec.shape))
var_x2=np.zeros(max(tvec.shape))
sigma3_x1=np.zeros(max(tvec.shape))
sigma3_x2=np.zeros(max(tvec.shape))


for ct in range(0,max(tvec.shape)):
    var_x1[ct] = gpc_covariance(Norm_psi,np.transpose(coeff_x1[:,ct]))
    var_x2[ct] = gpc_covariance(Norm_psi,np.transpose(coeff_x2[:,ct]))
    sigma3_x1[ct] = 3*math.sqrt(var_x1[ct])
    sigma3_x2[ct] = 3*math.sqrt(var_x2[ct])

###############################################################################
## Plots
###############################################################################

fig1 = plt.figure(num=1, figsize = (10,6),dpi = 300)
plt.subplot(2,2,1)
plt.plot(tvec,x1_mean,'b-',linewidth=1.2,label = u'Mean')
plt.plot(tvec,(x1_mean + sigma3_x1),'r--',linewidth=0.8,label = u'3-$\sigma$ bound')
plt.plot(tvec,(x1_mean - sigma3_x1),'r--',linewidth=0.8)
plt.xlabel('Time [s]')
plt.ylabel('Position $x_1$ [m]')
plt.legend(loc = 'upper right',fontsize = 8)

plt.subplot(2,2,2)
plt.plot(tvec,x2_mean,'b-',linewidth=1.2,label = u'Mean')
plt.plot(tvec,(x2_mean + sigma3_x2),'r--',linewidth=0.8,label = u'3-$\sigma$ bound')
plt.plot(tvec,(x2_mean - sigma3_x2),'r--',linewidth=0.8)
plt.xlabel('Time [s]')
plt.ylabel('Velocity $x_2$ [m]')
plt.legend(loc = 'upper right',fontsize = 8)
plt.show()

+-----------------------------------------------------------------------------------------------------------
| Sample ODE Module for Mass Spring Damper System
+-----------------------------------------------------------------------------------------------------------

def ode(t,x0,param): 
    
    x1_dot = x0[1]
    x2_dot = -(param.c/param.m)*x0[1]-(param.k/param.m)*x0[0]
 
    return([x1_dot,x2_dot])

 


+-----------------------------------------------------------------------------------------------------------
| Sample Main Module 2

	For uncertainty propagation in open loop UAV
 
+-----------------------------------------------------------------------------------------------------------

from gpc_essentials import gpc_essentials
from gpc_covariance import gpc_covariance
from gpc_coefficients_cal import gpc_coefficients_cal
from msg_quadrature import msg_quadrature
from gaussian_transformation import gaussian_transformation
from uniform_transformation import uniform_transformation
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from ode import ode
import math
import numpy as np
from scipy.io import savemat


class MSG:
   
    P = 5               # Polynomial Chaos Order
    d = 7               # Dimensions of uncertain variables
    d_Gaussian = 2      # Number of Gaussian random variables
    d_Uniform = 5       # Number of Uniform random variable
    L = 6               # Maximum accuracy level

class Parameter:
   
    g = 9.81  	        #acceleration due to gravity m/s^2
    rho = 1.225	        #air density Kg/m^3
    lamda_n = 0.15
    lamda_p = 0.15
    lamda_y = 0.15

  
class Uncertainty:      # Normally distributed

    mu = np.array([0,0])    # Mean vector of initial position along x(east) 
                            # and along y (north)
    sig = np.array([0.01,0.01]) # Sigma vector of initial position along x(east) 
                            # and along y (north)
       
    # Uncertain Variable with Uniform Distribution
    # Specify a vector of lower bounds of the uniformly distributed 
    # random variables
    
    lb = np.array([3,0.04,0.0175,0.41,2.75])  # lower bound of m,C_d0,k,S and T_max
    
    # Specify a vector of upper bounds of the uniformly distributed random variables
    
    ub = np.array([4.25,0.065,0.0225,0.615,5]) # lower bound of m,C_d0,k,S and T_max

######################
## Creating Objects
######################

msg = MSG()
param= Parameter()
uc = Uncertainty()

#######################
# Other parameters
#######################

## Initial conditions
H0 = 250
E0 = 270
chi_0 = math.pi/3     

eta_0 = 1   
gamma_0 = 0   
a_p0 = param.g
a_pc = a_p0
a_y0 = 0
eta_com = 0.4

###############################################################################
## Time vector for integration
###############################################################################

dt = 0.1
tvec = np.arange(0,900+dt,dt)

###############################################################################
## Obtain the nodes and weights from mixed sparse grid quadrature
###############################################################################

[nodes,w] = msg_quadrature(msg)       

Q= max(nodes.shape);   # Total sample size		      

print('==========  Generated MSG Nodes and Weights  ==========')
print('\n');
print(' Number of MSG Nodes generated = %d', Q)

###############################################################################
## Essentials of gPC expansion
###############################################################################

[Norm_psi, N, V_gpc , phi] = gpc_essentials(msg,nodes)   

print('==========  Generated essentials of gPC expansion  ==========');

###############################################################################
##Gaussian Affine Transformation
###############################################################################

x_G = gaussian_transformation(uc.mu, uc.sig ,nodes, msg.d_Gaussian)

###############################################################################
## Adjustment for uniformily distributed parameters
###############################################################################

x_U = uniform_transformation(uc.lb,uc.ub,nodes,msg.d_Gaussian,msg.d_Uniform)      


m = x_U[:,0]
C_d0 = x_U[:,1]
k = x_U[:,2]
S = x_U[:,3]
T_max = x_U[:,4]
###############################################################################
## Obtain the solution of quantities of interest
###############################################################################

# Buffer

x1 = np.zeros([len(tvec),Q])
y1 = np.zeros([len(tvec),Q])

for cc in range(0,Q):
    W = m[cc]*param.g
    X0 = [x_G[cc,0],x_G[cc,1],H0,E0,gamma_0,chi_0,eta_0,a_p0,a_y0]     
    params= [param.g,param.rho,S[cc],C_d0[cc],W,k[cc],T_max[cc],param.lamda_n,param.lamda_p,param.lamda_y,eta_com,a_pc]
    X1 = solve_ivp(ode,[tvec[0],tvec[-1]],X0,method='RK45',t_eval = tvec,args=(params,),vectorized = True)#,rtol = 1e-3,atol = 1e-7)     # replace ode with the name of ode_module
    x1[:,cc] = X1.y[0,:]
    y1[:,cc] = X1.y[1,:]

  
###############################################################################
## Post processing
###############################################################################
   
# gPC coefficients calculation of propagated collocation points
    
coeff_x1 = gpc_coefficients_cal(Norm_psi,phi,w,x1)
coeff_y1 = gpc_coefficients_cal(Norm_psi,phi,w,y1)

###################################
# Mean and Variances Calculation
###################################
# Mean 
#########

x1_mean = coeff_x1[0, :]
y1_mean = coeff_y1[0, :]

#############################
## Variance
#############################
# Buffer

var_x1=np.zeros(max(tvec.shape))
var_y1=np.zeros(max(tvec.shape))
sigma3_x1=np.zeros(max(tvec.shape))
sigma3_y1=np.zeros(max(tvec.shape))


for ct in range(0,max(tvec.shape)):
    var_x1[ct] = gpc_covariance(Norm_psi,np.transpose(coeff_x1[:,ct]))
    var_y1[ct] = gpc_covariance(Norm_psi,np.transpose(coeff_y1[:,ct]))
    sigma3_x1[ct] = 3*math.sqrt(var_x1[ct])
    sigma3_y1[ct] = 3*math.sqrt(var_y1[ct])
    
#############################
## Covariance
#############################
# Buffer   

covv_xy1 = np.zeros([len(tvec),2,2])

for cm in range (0,len(tvec)):
    covv_xy1[cm,:,:]= gpc_covariance(Norm_psi,np.array([np.transpose(coeff_x1[:,cm]),np.transpose(coeff_y1[:,cm])]))
    
###############################################################################
## Plots
###############################################################################


savemat("veh_1_py.mat",{"x_mean_p1":x1_mean,"y_mean_p1":y1_mean,"covv_x_y_py1":covv_xy1})


# Note: User can use veh_1_py.mat to plot 3D trajectory and 3-sigma ellipse.

+-----------------------------------------------------------------------------------------------------------
| Sample ODE Module for UAV
 
+-----------------------------------------------------------------------------------------------------------
  
import math as math
import numpy as np
   
def ode(t,xi,p):
    
    # Assigning variable
    [g,rho,S,C_d0,W,k,T_max,lamda_n,lamda_p,lamda_y,eta_com,a_pc]= p
   
    [x,y,H,E,gamma,chi,eta,a_p,a_y] = xi
    
    if (2*g*(E-H)<0):
        V = math.sqrt(2*g*abs(E-H))
    else:
        V= math.sqrt(2*g*(E-H))
    T = eta*T_max # Thrust
    n = (1/g)*math.sqrt(a_p**2+a_y**2)
    D0 = (1/2)*rho*(V**2)*S* C_d0  #skin friction drag
    Di = k*((W/(0.5*rho*(V**2)*S))**2)   #induced drag
    D = D0 + (n**2)*Di   ## Total drag

    if t<=3*60:
        a_yc = 0*g
        
    elif t>3*60 and t<=5.5*60:
        a_yc = 0.01*g
    else:
        a_yc = 0*g
  
    x_dot= V*np.cos(gamma)*np.cos(chi)
    y_dot= V*np.cos(gamma)*np.sin(chi)
    H_dot = V*np.sin(gamma)
    E_dot = (V/W)*(T-D)
    gamma_dot = (1/V)*(a_p-g*np.cos(gamma))
    chi_dot = (a_y/(V*np.cos(gamma)))
    eta_dot = (-lamda_n*(eta - eta_com))
    a_p_dot = (-lamda_p*(a_p - a_pc))
    a_y_dot = (-lamda_y*(a_y - a_yc)) 
    
    
    return([x_dot,y_dot,H_dot,E_dot,gamma_dot,chi_dot,eta_dot,a_p_dot,a_y_dot])
