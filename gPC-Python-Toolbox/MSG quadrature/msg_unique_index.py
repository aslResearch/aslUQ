import numpy as np
from msg_total import msg_total
from compute_order import compute_order
from comp_next import comp_next
from vec_colex_next3 import vec_colex_next3
from KPN_compute_points import KPN_compute_points
from KPU_compute_points import KPU_compute_points
from r8col_undex import r8col_undex


def msg_unique_index(d, L, vec_rules):
    
#   This function maps nonunique points to unique points
# Input: (i) d = dimension of uncertainty
#       (ii) L = accuracy level       
#        (iii) vec_rules = vector of 1D rules

#  Special cases.
    if ( L < 0 ):
        sparse_unique_index = []
        return(sparse_unique_index)
    
    if ( L == 0 ):
        sparse_unique_index[0] = 1
        return(sparse_unique_index)
    
    # Get total number of points, including duplicates.

    point_total_num = msg_total(d, L, vec_rules)
    
    #  Generate SPARSE_TOTAL_ORDER and SPARSE_TOTAL_INDEX arrays for the TOTAL set of points.

    sparse_total_order = np.zeros((d,int(point_total_num)))
   
    sparse_total_index = np.zeros((d,int(point_total_num)))

    point_total_num2 = 0

    # The outer loop generates values of LEVEL.

    level_min = max(0, L + 1 - d )

    for level in range (level_min,L+1):
    # The middle loop generates a GRID, based on the next partition 
    # that adds up to LEVEL.
    
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
                [point_index, more_points ] = vec_colex_next3 ( d, order_1d, point_index, more_points)
            
                if not more_points:
                    break
                
        
                point_total_num2 = point_total_num2 + 1
                sparse_total_order[0:d,(point_total_num2-1)] = order_1d[0:d]
                sparse_total_index[0:d,(point_total_num2-1)] = point_index[0:d]
        
            if not more_grids:
                break
            
    ## Now compute the coordinates of the TOTAL set of points.
    
    sparse_total_point = 1.0E+30*np.ones((d, int(point_total_num)))
    
    for dim in range(0,d):
        for level in range(0,L+1):
            order = compute_order(1,np.array([[level]]), vec_rules[dim])
            
            if ( vec_rules[dim] == 1 ):
                points = KPN_compute_points(level)
            elif ( vec_rules[dim] == 2 ):
                points = KPU_compute_points(level)
            
            index = np.array(np.where(sparse_total_order[dim,0:int(point_total_num)] == int(order[0])))
            
            for i in range(0,index.size):
                
                sparse_total_point[dim,int(index[0,i])] = points[int(sparse_total_index[dim,int(index[0,i])])-1,0]
            
            
        
    
#  Now determine the mapping from nonunique points to unique points.
#  We can not really use the UNDX output right now.

    
    sparse_unique_index = r8col_undex ( d, point_total_num, sparse_total_point)
    
    
    return(sparse_unique_index)