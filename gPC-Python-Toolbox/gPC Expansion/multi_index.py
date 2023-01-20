import math
import numpy as np
from Indexes import Indexes
dist={}

def multi_index(P,D,syschar):
    
# This function computes the normalization coefficients, total
# multi-dimensional order of gPC expansion, and reverse-graded lexocgraphic
# indexing of gPC orders in each dimension of uncertainty

# Inputs:
#       (i) P = order of gPC expansion
#       (ii) D = total number of uncertain variables
#       (iii) syschar = string of characters representing orthogonal
#                       polynomials ('H' for Hermite, 'P' for Legendre)

# Input Example:
# For problem with 4 uncertain variables (2 Gaussian and 2 uniform) and 4th
# order gPC expansion
# P = 4, D = 4, syschar = 'HHPP'

# Outputs:
#       (i) N = order of gPC expansion (singly-indexed) obtained from
#                lexicographic ordering = nchoosek(P+D,P) 
#       (ii) Norm_psi = vector of normalization coefficients (1 x N array)
#       (iii) indexes = multi-dinsional indexing (N x D array) 
      

    normalization_coeff = 0

# Extract the polynomial type and store in a variable 'dist'.
    for ct in range(0,D):
        if syschar[ct]=="P":
            dist[ct]=np.array("uniform") ##dtype=[("name", (np.str_, 10))])
        elif syschar[ct]=="H":
            dist[ct]=np.array("normal") ## dtype=[("name", (np.str_, 10))])

# Check if length 'dist' is equal to the dimension of uncertainty

    if D!=len(dist):
        print("Dimension Mismatch")
    
# Compute indexes and order  

    [indexes,N]=Indexes(P,D);
    
    # NORM FOR the Legendre and hermite Polynomials
    # One dimensional normalization constants
    
    norm_legendre = lambda n: 1/(2*n+1)
    norm_hermite = lambda n: math.factorial(n) 
    
    # Buffer for multidimensional normalization coefficient.
    Norm_psi = np.ones([1,N],float)
    
    # Outer loop for each polynomial order
    for l in range(0,N):
        
        # Inner loop for each dimension of uncertainty type
        
        for cd in range (0,D):
            
            # Extract the string "uniform" and "normal"
            distribution_type=dist[cd]
            if (distribution_type == "uniform"):
                normalization_coeff=norm_legendre(indexes[l,cd])
            elif (distribution_type == "normal"):
                normalization_coeff=norm_hermite(indexes[l,cd])
            else:
                print("Error: Enter random variables with either Uniform or Gaussian distribution")
           
            # Normalization constant is the multidimensional product. 
            Norm_psi[0,l]=Norm_psi[0,l]*normalization_coeff
    
    return([Norm_psi, N, indexes])
    
    
