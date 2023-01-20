import numpy as np
from kpn_order import kpn_order
from kpu_order import kpu_order

def compute_order (d,q,vec_rules):
    
    ## Compute the order of polynomials based on accuracy level (q)
    
    order = np.zeros((d))
    

    for ind_dim in range (0,d):
        if(vec_rules[ind_dim]==1):
            if(q[0,ind_dim] ==0):
                order[ind_dim] = 1  # order is 1 if accuracy level is 0
            else:
                order[ind_dim] = kpn_order(q[0,ind_dim])  # use function kpn_order for other accuracy levels
        elif (vec_rules[ind_dim] ==2):
            if(q[0,ind_dim] ==0):
                order[ind_dim] = 1  # order is 1 if accuract level is 0
            else:
                order[ind_dim] = kpu_order(q[0,ind_dim])  # use function kpu_order for other accuracy levels 
    
    return(order)
    
    
    
    
