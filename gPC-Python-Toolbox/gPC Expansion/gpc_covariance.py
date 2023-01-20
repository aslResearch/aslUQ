# gpc_covariance: This function computes covariance between two random
#                 processes (a and b), given the coefficients of gPC 
#                 expansion (a_c and b_c ) of both a and b.
#                 Instead, if b_c is not provided or empty, the function 
#                 computes the auto-covariance of random process a.

# Inputs: (variable number of arguments can be passed from calling environment in arg)
#       (i) nrm = gPC Normalization coefficients (1 x N array)
#       (ii) a_c = gPC coefficients of random process a (1 x N array)
#       (iii) b_c = gPC coefficients of random process b (1 x N array)

# Output:
#        covv = covariance between a and b if coefficient of gPC expansion for both
#               a and b is provided (2 x 2 array), autocovariance of a if 
#               b_c is not provided (scalar)


import numpy as np
def gpc_covariance(*arg):
    nrm = arg[0]
    
    a_c = arg[1]
    
    # If b_c is not specified, we equate b_c = a_c and compute the (auto-)
    # covariance of a

    if (len(arg)<3):      # b_c and a_c must be numpy array.
        b_c = a_c
    else:
        b_c = arg[2]
    
    # Weighted inner product
            
    #        i) a_c[0:,1:] and b_c[0:,1:] are extraction of 2nd to Nth order
    #           gPC coefficients
    #        ii) np.diag(nrm[0,1:]) gives diagonal Normalization matrix (N-1 x N-1 array)   
   
    if a_c.shape[0]==2:
     
        covv = np.dot(np.dot(a_c[0:,1:],np.diag(nrm[0,1:])),
                  np.transpose(b_c[0:,1:]))
    else:
        covv = np.dot(np.dot(a_c[1:],np.diag(nrm[0,1:])),
                  np.transpose(b_c[1:]))
    return(covv)



