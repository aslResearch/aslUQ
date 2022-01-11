import numpy as np
from hermite_poly import hermite_poly
from legendre_shifted_poly import legendre_shifted_poly
dist={}
def gpcbasis_evaluate(V,xi):
    
    syschar = V[0]
    indexes = V[1]
   
    N=np.size(indexes,0) # find number of rows in indexes

    Q=np.size(xi,0)
    D=np.size(xi,1)
   
    for ct in range(0,D):
        if syschar[ct]== "P":
            dist[ct]=np.array("uniform") ##dtype=[("name", (np.str_, 10))])
        elif syschar[ct]=="H":
            dist[ct]=np.array("normal") ## dtype=[("name", (np.str_, 10))]) 

## Basis Evaluation FOR the Legendre and hermite Polynomials at xi nodes 
    
    basis_val=np.zeros([N,max(xi.shape)],float)  
            
    for cl in range(0,N):
           dum_val=1
           for cd in range (0,D):
               distribution_type=dist[cd]
               if (distribution_type == "uniform"):
                   basis_eval = legendre_shifted_poly((indexes[cl,cd]),xi[:,cd])
                   
               elif (distribution_type == "normal"):
                   basis_eval = hermite_poly((indexes[cl,cd]),xi[:,cd])
                   
               else:
                   print("Error: Enter random variables with either Uniform or Gaussian distribution")
               dum_val=np.multiply(dum_val,np.array([basis_eval]))
                          
           basis_val[cl,:]= dum_val 
           
    return(basis_val)



