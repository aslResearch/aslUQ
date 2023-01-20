import numpy as np
from msg_size import msg_size
from msg_unique_index import msg_unique_index
from msg_index import msg_index
from msg_point import msg_point
from msg_weight import msg_weight
def msg_quadrature(msg):
    
    # Generates nodes and weights of mixed sparse grid rule
    # Input: msg class
    #        (i) d = dimension of uncertainty
    #        (ii) L = accuracy level       
    #        (iii) d_Gaussian = dimension of Gaussian variables
    #        (iv) d_Uniform = dimension of Uniform variables
    # Note that d = d_Gaussian + d_Uniform
    
    d = msg.d
    L = msg.L
    d_Gaussian = msg.d_Gaussian
    d_Uniform = msg.d_Uniform
    
    # Check if d = d_Gaussian + d_Uniform.
    if d!= (d_Gaussian + d_Uniform):
        print("Sum of Gaussian and Uniform random variable should be equal to d.")
        print("ERROR: dimension mismatch")
        return
    
    # Stack the rules based on number of gaussian and uniform random variables
    # 1 for Kronrod-Patterson Gaussian rule
    
    rule_KPN = 1
    
    # 2 for Kronrod-Patterson Uniform rule
    rule_KPU = 2 
    
    # Vector of rules
    vec_rules_1 = rule_KPN * np.ones((d_Gaussian,1))
    vec_rules_2 = rule_KPU * np.ones((d_Uniform,1))   
    vec_rules= np.concatenate((vec_rules_1,vec_rules_2),axis = 0)  
    
    # Compute number of msg points
    point_num = msg_size(d,L,vec_rules)    
    
    # Compute unique indices for sparse points
    sparse_unique_index = msg_unique_index(d, L, vec_rules )
    
    # Compute order and required sparse indices
    [sparse_order,sparse_index] = msg_index(d, L, vec_rules, point_num, sparse_unique_index)
    
    # Compute nodes and weights
    pts = msg_point(d, L, vec_rules, point_num, sparse_order, sparse_index )
   
    wts = msg_weight(d, L, vec_rules, point_num, sparse_unique_index )
    
    # Return mixed sparse grid nodes and weights
    nodes = np.transpose(pts)
    weights = np.transpose(wts)
    
    return([nodes,weights])



