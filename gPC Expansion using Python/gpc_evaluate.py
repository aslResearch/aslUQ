import numpy as np
def gpc_evaluate(a_i_alpha,V,xi):
    # check whether arguments a_i_alpha, I_a and xi match
    # evaluate the gpc basis functions
   
    from gpcbasis_evaluate import gpcbasis_evaluate
    y_alpha_j = gpcbasis_evaluate(V,xi)

    # multiply with gpc coefficients
    # N x k : (N x M) * (M x k)

    a_i_j = np.dot(np.transpose(a_i_alpha),y_alpha_j)
    return(a_i_j)




