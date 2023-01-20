import numpy as np
from hermite_poly import hermite_poly
from legendre_shifted_poly import legendre_shifted_poly
dist={}
def gpcbasis_evaluate(V,xi):

# This function computes basis of gPC expansion at quadrature nodes.

# Inputs:
#       (i) V = Cell array with two cells (1 and 2). 
#               Cell 1 contains 'syschar', a string of characters representing orthogonal
#                       polynomials ('H' for Hermite, 'P' for Legendre)
#               Cell 2 contains 'indexes', multi-dinsional indexing (D x N array)
#               D: total number of uncertain variables 
#               N: order of gPC expansion (singly-indexed) obtained from
#                  lexicographic ordering
#       (ii) xi =  Quadrature Grid obtained directly from quadrature
#                  technique (N_q x D array), where N_q is the grid size

# Input Example:
# For problem with 4 uncertain variables (2 Gaussian and 2 uniform) and 4th order gPC expansion
# P = 4, D = 4, syschar = 'HHPP', N = nchoosek(P+D,P) = 70
# V[0] = 'HHPP'
# V[1] = indexes (70 x 4 array)

# Output:
#       basis_val = basis of gPC expansion at quadrature nodes (N x N_q array)

# Extract the essentials from the input    
    syschar = V[0]
    indexes = V[1]
   
    N = np.size(indexes,0) # find number of rows in indexes

    N_q = np.size(xi,0)
    D = np.size(xi,1)

# Extract the polynomial type and store in a variable 'dist'.

    for ct in range(0,D):
        if syschar[ct]== "P":
            dist[ct]=np.array("uniform") ##dtype=[("name", (np.str_, 10))])
        elif syschar[ct]=="H":
            dist[ct]=np.array("normal") ## dtype=[("name", (np.str_, 10))]) 

## Basis Evaluation FOR the Legendre and hermite Polynomials at xi nodes 
    
    basis_val=np.zeros([N,max(xi.shape)],float)  # Buffer
    
    # Outer loop for each polynomial order       
    for cl in range(0,N):
           dum_val=1
           
           # Inner loop for each dimension of uncertainty type
           for cd in range (0,D):
               
               # Extract the string "uniform" and "normal"
               distribution_type=dist[cd]
               if (distribution_type == "uniform"):
                   basis_eval = legendre_shifted_poly((indexes[cl,cd]),xi[:,cd])
                   
               elif (distribution_type == "normal"):
                   basis_eval = hermite_poly((indexes[cl,cd]),xi[:,cd])
                   
               else:
                   print("Error: Enter random variables with either Uniform or Gaussian distribution")
               
               # Basis function is the multidimensional product.
               
               dum_val = np.multiply(dum_val,np.array([basis_eval]))
                          
           basis_val[cl,:]= dum_val 
           
    return(basis_val)



