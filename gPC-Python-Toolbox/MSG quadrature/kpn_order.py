def kpn_order(l):
    
# This function computes the order of a KPN rule from the level.
# Inputs: L=  accuracy level of the rule (1 <= L <= 25)

    if (l<1):
        print("KPN order error")
        print("1<=L<=25 required")
        print("Input l = ",l)
        return
    elif (l==1):
        n = 1
    elif (l<=3):
        n = 3
    elif (l==4):
        n = 7
    elif (l<=8):
        n = 9
    elif (l==9):
        n = 17
    elif (l<=15):
        n = 19
    elif (l==16):
        n = 31
    elif (l==17):
        n = 33
    elif (l<=25):
        n = 35
    else:
        print('KPN order error- 1 <=L <=25 required')
        print("Input l = ",l)
    return(n)
        