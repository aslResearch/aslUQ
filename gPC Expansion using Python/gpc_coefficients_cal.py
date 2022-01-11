def gpc_coefficients_cal(Norm_psi,phi,w,x):
    
    import numpy as np
    phi_t= np.transpose(phi)               #transpose of phi
    sum_all_x1 = np.dot(x,(w*phi_t))      #element wise multiplication
   
    gpc_coeff= (1/Norm_psi)*sum_all_x1
    
    return(np.transpose(gpc_coeff))