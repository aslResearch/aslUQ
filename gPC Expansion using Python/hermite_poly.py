import numpy as np

def hermite_poly(*arg):
    global h
    n=arg[0]
    x=arg[1]
    
    #HERMITE:  compute the probabilist Hermite polynomials of degree n.
    #           x optional values where we want to evaluate the hermite polynomial of degree n
    # call the hermite recursive function.
    h = hermite_rec(n)
    
       # evaluate the hermite polynomial function, given x
    if(len(arg)==2):
   
       y=(h[0,(max(np.shape(h)))-1])*(np.ones(x.shape,float))  
       j=1
       for i in range(max(np.shape(h))-1,0,-1):
           y = y+(h[0,i-1] * np.power(x,j))
           j=j+1
       # restore the shape of y, the same as 
       h=np.reshape(y,x.shape)
    return(h)

def hermite_rec(n):
    import numpy as np
    global h
    # This is the reccurence construction of the probabilist Hermite polynomial, i.e.:
    #   He_0(x) = 1
    #   He_1(x) = x
    #   He_[n+1](x) = x He_n(x) - n He_[n-1](x)
    # 0th case
    
    if(n==0):
        h=(np.array([[1]]))
    elif(n==1):
        h=(np.array([[1,0]])) 
    else:
        # He_[n-1](x)
        h1=np.zeros([1,int(n+1)],float)
        h1[0,0:int(n)]=hermite_rec(n-1)
        # He_[n-2](x)
        h2 = np.zeros([1,int(n+1)],float)
        h2[0,2:]=(n-1)*hermite_rec(n-2)
        # He_[n](x)
        h = h1 - h2
    return(h)




           

    


 

