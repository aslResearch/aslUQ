import numpy as np
from compute_order import compute_order
from KPN_compute_points import KPN_compute_points
from KPU_compute_points import KPU_compute_points

def msg_point(d, L, vec_rules, point_num, sparse_order, sparse_index):
    
#   This function computes the points of a sparse grid rule.
#   Inputs: (i) point_num = the number of unique points in the grid.
#           (ii) d = dimension of uncertainty
#           (iii) L = accuracy level
#            (iv) vec_rules = vector of 1D rules

#   Output: sparse points

# Compute the point coordinates.
    sparse_point = 1.0E+30*np.ones((d, int(point_num))) # assigning huge number
    
    for dim in range(0,d):
        for level in range(0,L+1):
            order = compute_order(1,np.array([[level]]), vec_rules[dim])
            
            if ( vec_rules[dim] == 1 ):
                points = KPN_compute_points (level)
            elif ( vec_rules[dim] == 2 ):
                points = KPU_compute_points (level)
            
            index = np.array(np.where(sparse_order[dim,0:int(point_num)] == int(order[0])))
            
            
            for i in range(0,index.size):
                
                sparse_point[dim,int(index[0,i])] = points[int(sparse_index[dim,int(index[0,i])])-1,0]
            
            
                  
    return (sparse_point)
