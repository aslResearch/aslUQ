import numpy as np
def legendre_shifted_poly(*arg):
    global p
    n=(arg[0])
    x=arg[1]
    # LEGENDRE: compute the Legendre polynomials of degree n.
    #           x optional values where we want to evaluate the Legendre
    #           polynomial of degree n
    # THIS FUNCTION BUILD THE MONIC VERSION OF LEGENDRE POLYNOMIALS 
    # IT SHOULD BE APPLIED WITH GAUSS LEGENDRE quadrature

    # Inputs:
    #   - n is the order of the Legendre polynomial (n>=0).
    #   - x is (optional) values to be evaluated on the resulting Legendre
    #     polynomial function.

    # call the hermite recursive function.
    
    p = legendre_rec(n)
    
    #evaluate the legendre polynomial functon, given x
    if(len(arg)==2):
        y=(p[0,max(np.shape(p))-1])*(np.ones(x.shape,float))
        j=1
        for i in range(max(np.shape(p))-1,0,-1):
            y=y+(p[0,i-1]*np.power(x,j))
            
            j=j+1
        #restore the shape of y, the same as x
        p = np.reshape(y,x.shape)   
     
    return(p)
def legendre_rec(n):
    global p
    # This is the reccurence construction of Legendre polynomials, i.e.:
    #   P0(x) = 1
    #   P1(x) = x
    #   P[n+1](x) = x Pn(x) - (n^2)/(4n^2-1) P[n-1](x) 
    
    if(n==0):
        p=(np.array([[1]]))
      
    elif(n==1):
        p=(np.array([[2,-1]])) 
    else:
        p1 = np.zeros([1,int(n+1)],float)
        p1[0,0:int(n)]=(4*(n-1)+2)/n*legendre_rec(n-1)
        
        p2 = np.zeros([1,int(n+1)],float)
        p2[0,1:]=(2*(n-1)+1)/n*legendre_rec(n-1)
        
        p3= np.zeros([1,int(n+1)],float)
        p3[0, 2:]=((n-1))/(n)*legendre_rec(n-2)
        
        p = p1-p2-p3;
    return(p)
        
