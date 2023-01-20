###############################################################################
### This is sample main_module for uncertainty quantification in Mass Spring
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

# x_U = uniform_transformation(uc.lb,uc.ub,nodes,msg.d_Gaussian,msg.d_Uniform)


###############################################################################
## Obtain the solution of quantities of interest
###############################################################################

# Buffer
x1 = np.zeros([len(tvec),Q])
x2 = np.zeros([len(tvec),Q])

for cc in range(0,Q):
    
    X0 = [x_G[cc,0],x_G[cc,1]]     # Initial Conditions
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



