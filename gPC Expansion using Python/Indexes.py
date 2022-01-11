import math

def nchoosek(n, k):
    return math.factorial(n) /( math.factorial(k)* math.factorial(n - k))

def Indexes(P,D):
    import numpy as np
    # This function creates a vector of indexes for the degrees of the different 
    # orthogonal polynomials.
    # P  maximum value inside indexes (i.e maximum degree for a specific direction)
    # D    Stochastic dimension of the problem 
   
    N = int(nchoosek(P+D,P))
    
    indexes= np.zeros([int(N),int(D)])
    v = np.ones([1,D],int)
    for s in range(0,N):
        indexes[s,0:(D-1)]=-np.diff(v,axis=1)
        indexes[s,D-1]= v[0,D-1]-1
     ## Update index vector:
        for k in range(D,0,-1):
             v[0,k-1]=v[0,k-1]+1;
             if k>1:
                 if v[0,k-1]<=v[0,k-2]:
                     break
                 v[0,k-1]=1
    return([indexes,N])


