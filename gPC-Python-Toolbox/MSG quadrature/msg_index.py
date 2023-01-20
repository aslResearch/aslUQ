import numpy as np
from comp_next import  comp_next
from compute_order import compute_order
from vec_colex_next3 import vec_colex_next3

def msg_index (d, L, vec_rules, point_num, sparse_unique_index ):
    
#    This function returns the order and index for each unique point in the sparse grid.
#    Inputs: (i) point_num, the number of unique points in the grid.
#            (ii) sparse_unique_index, associates each point in the grid with its unique representative.
#            (iii) d = dimension of uncertainty
#            (iv) L = accuracy level
#            (v) vec_rules= vector of 1D rules

# Special cases.
    
    if ( L < 0 ):
        sparse_order = []
        sparse_index = []
        return([sparse_order,sparse_index])
    
    if ( L == 0 ):
        sparse_order[0:d,0] = 1
        sparse_index[0:d,0] = 1
        return([sparse_order,sparse_index])
    
    sparse_order = np.zeros( (d, point_num) )
    sparse_index = np.zeros( (d, point_num) )
    
    point_count = 0

#  The outer loop generates values of LEVEL.

    level_min = max ( 0, L + 1 - d )
    
    for level in range (level_min,L+1):
        
#  The middle loop generates a GRID,
#  Based on the next partition that adds up to LEVEL.

        level_1d = []
        more_grids = 0
        h = 0
        t = 0
        
        while 1:
            [level_1d,more_grids,h,t] = comp_next(level, d, level_1d, more_grids, h, t )
            
            order_1d = compute_order ( d, level_1d, vec_rules )
  
            # The inner loop generates a POINT of the GRID of the LEVEL.

            point_index = []
            more_points = 0
            
            while 1:

                [point_index, more_points] = vec_colex_next3 ( d, order_1d, point_index, more_points )
                if not more_points:
                    break
                
                point_count = point_count + 1
                
                point_unique = int(sparse_unique_index[point_count-1])
                sparse_order[0:d,point_unique-1] = order_1d[0:d]
                sparse_index[0:d,point_unique-1] = point_index[0:d]

            if not more_grids:
                break
            
    return([sparse_order,sparse_index])