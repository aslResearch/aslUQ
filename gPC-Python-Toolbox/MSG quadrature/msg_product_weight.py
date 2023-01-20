import numpy as np

from KPN_compute_weights import KPN_compute_weights
from KPU_compute_weights import KPU_compute_weights
from r8vec_direct_product2 import r8vec_direct_product2

def msg_product_weight(d, level_1d, order_1d, order_nd, vec_rules):
    
# This function computes the weights of a mixed product rule.
# Inputs: (i) d = dimension of uncertainty
#         (ii) order_1d = order of 1D rules
#         (iii) level_1d = accuracy level of 1D rules
#         (iv) order_nd = order of product rule
#          (v) vec_rules = vector of 1D rules

## Product weight rule
    
    weight_nd = np.ones((1,int(order_nd)))
    
    for dim in range(0,d):
        if ( vec_rules[dim] == 1 ):
            weight_1d = KPN_compute_weights (level_1d[:,dim])
        elif ( vec_rules[dim] == 2 ):
            weight_1d = KPU_compute_weights (level_1d[:,dim])
        
        weight_nd = r8vec_direct_product2 ( dim, order_1d[dim], weight_1d, order_nd, weight_nd )
    
    return(weight_nd)