def rule_adjust(a,b,c,d,n,x,w):
    
    # This function takes the uniformly distributed quadrature nodes with the
    # PDF between ranges a and b and transforms it to collocation nodes with
    # the PDF between ranges c and d.
       
    for i in range(0,n):
        x[i]=((b-x[i])*c+((x[i]-a)*d))/(b-a)
    
    
    s=(d-c)/(b-a);
    
    w[0:n]=s*w[0:n]

    return([x,w])





