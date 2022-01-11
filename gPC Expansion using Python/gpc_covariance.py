import numpy as np
def gpc_covariance(*arg):
    nrm2=arg[0]
    a_i_alpha=arg[1]
    
    # if B is not specified we compute the (auto-) covariance of A

    if (len(arg)<3):      #b_j_alpha must be numpy array
        b_j_alpha= a_i_alpha
    else:
        b_j_alpha=arg[2]
    
    
    # compute weighted inner product between A and B giving the covariance 
    covv = np.dot(np.dot(a_i_alpha[1:],np.diag(nrm2[0,1:])),
                  np.transpose(b_j_alpha[1:]))
    
    return(covv)



