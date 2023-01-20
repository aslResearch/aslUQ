
def gaussian_transformation(mu_vec, sig_vec,xi, d_Gaussian):

# This function takes the normally distributed standard quadrature nodes with the
# mean vector of zeros and Covariance matrix of identity and transforms it to collocation nodes with
# the PDF N(mu_vec, Sigma) where mu_vec is the vector of mean and Sigma is a
# diagonal matrix of Variance, Sigma = diag(sig_vec.^2)

# Inputs:
#       (i) mu_vec = vector of mean of uncertain variables
#       (ii) sig_vec = vector of standard deviation of uncertain variables
#       (iii) xi = Quadrature Grid obtained directly from quadrature
#                technique (N_q x d array), where N_q is the grid size and
#                d is the total number of uncertain variables
#       (iv) d_Gaussian = number of Gaussian random variables

   
    Q_sg= max(xi.shape)
    x = xi[:,0:d_Gaussian]

    
    for i in range(0,Q_sg):
        for j in range(0,d_Gaussian):
            x[i,j] = mu_vec[j] + x[i,j] * sig_vec[j]
    
    return(x)