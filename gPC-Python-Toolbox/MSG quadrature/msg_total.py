import numpy as np
from comp_next import  comp_next
from compute_order import compute_order

def msg_total(d,L,vec_rules):
    
    # This function sizes (total points) a sparse grid, counting duplicate points.
    # Inputs: (i) d = dimension of uncertainty
    #         (ii) L = accuracy level
    #          (v) vec_rules = vector of 1D rules
  
  point_total_num = 0
  
#  The outer loop generates values of LEVEL.
#  Goes from L-n to L-1, instead go from L-n+1 to L. 
#  So level_min = level_max-dim_num+1, level_max=level_max

  level_min = max (0, L-d+1) 

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
      
          point_total_num = point_total_num + np.prod ( order_1d[0:d] )
          
          if not more_grids:
              break
    
  return(point_total_num)