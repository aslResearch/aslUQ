def rule_adjust(a,b,c,d,n,x,w):
    for i in range(0,n):
        x[i]=((b-x[i])*c+((x[i]-a)*d))/(b-a)
    
    
    s=(d-c)/(b-a);
    
    w[0:n]=s*w[0:n]

    return([x,w])





