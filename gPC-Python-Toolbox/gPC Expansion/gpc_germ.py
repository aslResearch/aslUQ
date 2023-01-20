import numpy as np
def gpc_germ(V, n_sample, D):
    
# gpc_germ function computes samples for evaluating gPC expansion of a stochastic process.

# Inputs:
#       (i) V = Cell array with two cells (1 and 2). 
#               Cell 1 contains 'syschar', a string of characters representing orthogonal
#                       polynomials ('H' for Hermite, 'P' for Legendre)
#               Cell 2 contains 'indexes', multi-dinsional indexing (D x N array)
#               D: total number of uncertain variables 
#       (ii) n_sample = number of samples required

# Input Example:
# For problem with 4 uncertain variables (2 Gaussian and 2 uniform) and 4th order gPC expansion
# P = 4, D = 4, syschar = 'HHPP', N = nchoosek(P+D,P) = 70
# V[0] = 'HHPP'
# V[1] = indexes (70 x 4 array)

# Output:
#       xi = Random sample points within standard distribution

# Extracting the necessary variables

    syschar = V[0]
    xi=np.zeros([n_sample,D],int)

    for ct in range(0,D):
        if syschar[ct]== "P":
            xi[:,ct]=np.transpose(np.array([np.random.uniform(0,1,n_sample)]))
        elif syschar[ct]== "H":
            xi[:,ct]=np.transpose(np.array([np.random.normal(0,1,n_sample)]))

    return(xi)

