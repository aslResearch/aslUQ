def kpu_order(l):
    
    # This function computes the order of a KPU rule from the level.
    # Inputs: L=  accuracy level of the rule (1 <= L <= 25)
 
    if (l<1):
        print("KPU order error")
        print("1<=L<=25 required")
        print("Input l = ",l)
        return
    elif (l==1):
        n = 1
    elif (l<=3):
        n = 3
    elif (l<=6):
        n = 7
    elif (l<=12):
        n = 15
    elif (l<=24):
        n = 31
    elif (l<=25):
        n = 63
    else:
        print("KPU order error- 1 <=L <=25 required")
    
    return(n)
        
        
        
       