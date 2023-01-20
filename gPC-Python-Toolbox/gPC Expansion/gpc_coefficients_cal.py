import numpy as np

def gpc_coefficients_cal(Norm_psi,phi,w,x):

# gpc_coefficients_cal: This function computes the coefficients of gPC expansion 
# for the solution of the variables at the collocation nodes.

# Inputs:
#       (i) Norm_psi = gPC Normalization coefficients (1 x N array)
#       (ii) phi = array of gPC basis evaluated at quadrature nodes 
#                  (N x Q array) where Q is the number of quadrature nodes
#       (iii) w = array of collocation weights (Q x 1 array)
#       (iv) x = solution of vector x at collocation nodes (n x Q
#                array), where n is the dimension of vector x.

# Output: 
#        Array of gPC coefficients of the variable x (N X N_x)

               
        phi_t= np.transpose(phi)  #transpose of phi
        sum_all_x1 = x @ (np.multiply(phi_t,w))      #element wise multiplication
        
        # gPC coefficient of the variable x
        gpc_coeff= np.multiply(np.true_divide(1,Norm_psi),sum_all_x1)
        
        return(np.transpose(gpc_coeff))