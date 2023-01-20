import numpy as np
def comp_next( n, k, a, more, h, t ):
    
    # This function computes the compositions of the integer N into K parts
    # i.e, a composition of the integer N into K parts is an ordered sequence
    # of K nonnegative integers which sum to N

# Inputs: (i) n =  the integer whose compositions are desired.
#         (ii) k = the number of parts in the composition.
#         (iii) a =  the previous composition.  On the first call, set a = []. 
#         (iv) more = boolean. On first call, set more = FALSE.
    
    if not more:
        t = n
        a = np.zeros((1,k))
        h = 0
        a[0,0] = n
        
        a[0,1:k] = 0
    else:
        if (1<t):
            h = 0
        h = h+1
        
        t = a[0,h-1]
        
        
        a[0,h-1] = 0
        a[0,0] = t - 1
        
        if a.size < h:
            a.resize(1,h+1)
        else:
            pass
        a[0,h] = a[0,h] + 1
        
    
    more = ((a[0,k-1])!=n)
    
    
    return([a,more,h,t])
