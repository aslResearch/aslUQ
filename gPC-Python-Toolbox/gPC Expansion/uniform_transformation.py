
def uniform_transformation(lower,upper,xi,d_Gaussian,d_Uniform):

# This function takes the uniformly distributed standard quadrature nodes with the
# PDF between ranges 0 and 1 and transforms it to uniformly distributed collocation nodes with
# the PDF between ranges-lower and upper.

# Inputs:
#       (i) lower = vector of lower bounds of uniformly distributed uncertain variables
#       (ii)upper = vector of upper bounds of uniformly distributed uncertain variables
#       (iii) xi = Quadrature Grid obtained directly from quadrature
#                technique (N_q x d array), where N_q is the grid size and
#       (iv) d_Gaussian = number of Gaussian random variables
#       (v) d_Uniform = number of Uniform random variables
  
    Q_sg= max(xi.shape)
    x = xi[:,d_Gaussian:d_Gaussian + d_Uniform]
    a = 0
    b = 1
    c = lower
    d = upper
    
    for i in range(0,Q_sg):
        for j in range(0,d_Uniform):
            x[i,j]=((b-x[i,j])*c[j]+((x[i,j]-a)*d[j]))/(b-a)
    
    
    return(x)