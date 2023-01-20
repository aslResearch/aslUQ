from msg_total import msg_total
from comp_next import  comp_next
from compute_order import compute_order
from vec_colex_next3 import vec_colex_next3
from KPN_compute_points import KPN_compute_points
from KPU_compute_points import KPU_compute_points

import numpy as np

def msg_size(d,L,vec_rules):
    
    # This function sizes (total points) a sparse grid made from mixed 1D rules.
    # Inputs: (i) d = dimension of uncertainty
    #         (ii) L = accuracy level
    #          (v) vec_rules = vector of 1D rules
    
    # Get total number of points, including duplicates
    point_total_num = msg_total(d,L,vec_rules)
    
        
    # Generate SPARSE_TOTAL_ORDER and SPARSE_TOTAL_INDEX arrays
    # for the TOTAL set of points.
    
    sparse_total_order = np.zeros((d,int(point_total_num)))
    
    sparse_total_index = np.zeros((d,int(point_total_num)))
    
    point_total_num2 = 0
    
    # The outer loop generates values of level.
    
    level_min = max (0,L+1-d)
    
    for level in range (level_min,L+1):
        
        # The middle loop generates a GRID, 
        # based on the next partition that adds up to LEVEL.
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
                
                [point_index, more_points ] = vec_colex_next3 ( d, order_1d,point_index, more_points)
                
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
                points = KPU_compute_points (level)
            
         
            index = np.array(np.where(sparse_total_order[dim,0:int(point_total_num)] == int(order[0])))
            
            
            for i in range(0,index.size):
                
                sparse_total_point[dim,int(index[0,i])] = points[int(sparse_total_index[dim,int(index[0,i])])-1,0]
            
            
        
    
    ##  Count the unique columns.
    _ , Mu_1 = np.unique(np.transpose(sparse_total_point), axis = 0,return_index = True)
    Mu = (np.transpose(sparse_total_point))[np.sort(Mu_1)]
    point_num = np.size(Mu,axis = 0)
    
    return(point_num)

            