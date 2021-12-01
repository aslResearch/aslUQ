function sparse_unique_index = msg_unique_index (d, L, vec_rules)
% This function maps nonunique points to unique points
% Input: (i) d = dimension of uncertainty
%        (ii) L = accuracy level       
%        (iii) vec_rules = vector of 1D rules

%%
%  Special cases.
%
  if ( L < 0 )
    sparse_unique_index = [];
    return
  end

  if ( L == 0 )
    sparse_unique_index(1) = 1;
    return
  end
  
%  Get total number of points, including duplicates.
%
  point_total_num = msg_total(d, L, vec_rules);
%
%  Generate SPARSE_TOTAL_ORDER and SPARSE_TOTAL_INDEX arrays for the TOTAL set of points.
%
  sparse_total_order = zeros(d, point_total_num);
  sparse_total_index = zeros(d, point_total_num);

  point_total_num2 = 0;
%
%  The outer loop generates values of LEVEL.
%
  level_min = max(0, L + 1 - d );

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

      order_1d = compute_order( d, level_1d, vec_rules);
%
%  The inner loop generates a POINT of the GRID of the LEVEL.
%
      point_index = [];
      more_points = 0;

      while ( 1 )

        [ point_index, more_points ] = vec_colex_next3 ( d, order_1d, ...
          point_index, more_points );

        if ( ~more_points )
          break
        end

        point_total_num2 = point_total_num2 + 1;
        sparse_total_order(1:d,point_total_num2) = order_1d(1:d);
        sparse_total_index(1:d,point_total_num2) = point_index(1:d);

      end

      if ( ~more_grids )
        break
      end

    end

  end
%
%  Now compute the coordinates of the TOTAL set of points.
%
  sparse_total_point = zeros ( d, point_total_num );
  sparse_total_point(1:d,1:point_total_num) = 1.0E+30;  % assign huge number

  for dim = 1 : d

    for level = 0 : L

      order = compute_order( 1, level, vec_rules(dim) );

      if ( vec_rules(dim) == 1 )
        points = KPN_compute_points ( level );
      elseif ( vec_rules(dim) == 2 )
        points = KPU_compute_points ( level );
      end

      index = find ( sparse_total_order(dim,1:point_total_num) == order );

      sparse_total_point(dim,index) = points ( sparse_total_index(dim,index) );

    end

  end
%
%  Now determine the mapping from nonunique points to unique points.
%  We can not really use the UNDX output right now.
%
  sparse_unique_index = r8col_undex ( d, point_total_num, sparse_total_point);

  return
end