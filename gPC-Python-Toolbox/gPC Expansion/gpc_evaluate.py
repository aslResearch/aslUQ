import numpy as np
from gpcbasis_evaluate import gpcbasis_evaluate
def gpc_evaluate(x_c,V,xi):

# This function evaluates the gPC expansion of the random process x at random grid points.

# Inputs:
#   (i) x_c = gPC coefficients of random process x (1 x N array)

#   (ii) V = Cell array with two cells (1 and 2). 
#               Cell 1 contains 'syschar', a string of characters representing orthogonal
#               polynomials ('H' for Hermite, 'P' for Legendre)
#               Cell 2 contains 'indexes', multi-dinsional indexing (D x N array)
#               D: total number of uncertain variables        

#    (iii) xi = Monte Carlo based randomly generated grid points for random variable x
#               (N_mc x 1 array) within the standard PDF (N(0, 1^2) for
#               standard Gaussian and U[0, 1] for standard Uniform).


# Input Example:
# For problem with 4 uncertain variables (2 Gaussian and 2 uniform) and 4th order gPC expansion
# P = 4, D = 4, syschar = 'HHPP', N = nchoosek(P+D,P) = 70
# V[0] = 'HHPP'
# V[1] = indexes (70 x 4 array)
# xi = Monte Carlo-based random sample points within standard distribution

# Outputs:
#       x_gpc = evaluation of gPC expansion of random variable x at MC grid points
   
# Determine the gpc basis functions at random grid points 
    
    phi_xi = gpcbasis_evaluate(V,xi)

# phi_xi need to be multiplied with x_c (gpc coefficients) to get gPC expansion evaluation
    
    x_gpc = np.dot(np.transpose(x_c),phi_xi)
    return(x_gpc)




