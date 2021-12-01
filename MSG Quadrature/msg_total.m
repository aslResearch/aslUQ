function point_total_num = msg_total( d, L, vec_rules )
% This function sizes a sparse grid, counting duplicate points.
% Input: (i) d = dimension of uncertainty
%        (ii) L = accuracy level       
%        (iii) vec_rules = vector of 1D rules

%% 
point_total_num = 0;
%
%  The outer loop generates values of LEVEL.
% Bin Jia goes from L-n to L-1, instead go from L-n+1 to L. 
% So level_min = level_max-dim_num+1, level_max=level_max
  level_min = max ( 0, L-d+1); 

  for level = level_min : L
%
%  The middle loop generates a GRID,
%  based on the next partition that adds up to LEVEL.
%
    level_1d = [];
    more_grids = 0;
    h = 0;
    t = 0;

    while ( 1 )

      [ level_1d, more_grids, h, t ] = comp_next(level, d, level_1d, more_grids, h, t );

      order_1d = compute_order( d, level_1d, vec_rules );

      point_total_num = point_total_num + prod ( order_1d(1:d) );

      if ( ~more_grids )
        break
      end

    end

  end

  return
end