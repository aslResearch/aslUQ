function [ sparse_order, sparse_index ] = msg_index (d, L, vec_rules, point_num, sparse_unique_index )

% This function return the order and index for each unique point in the
% sparse grid
%    Inputs: (i) POINT_NUM, the number of unique points in the grid.
%            (ii) SPARSE_UNIQUE_INDEX, associates each point in the grid with its unique representative.
%           (iii) d = dimension of uncertainty
%           (iv) L = accuracy level
%            (v) vec_rules= vector of 1D rules


%%
%  Special cases.
%
  if ( L < 0 )
    sparse_order = [];
    sparse_index = [];
    return
  end

  if ( L == 0 )
    sparse_order(1:d,1) = 1;
    sparse_index(1:d,1) = 1;
    return
  end

  sparse_order = zeros ( d, point_num );
  sparse_index = zeros ( d, point_num );

  point_count = 0;
%
%  The outer loop generates values of LEVEL.
%
  level_min = max ( 0, L + 1 - d );

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
%
%  The inner loop generates a POINT of the GRID of the LEVEL.
%
      point_index = [];
      more_points = 0;

      while ( 1 )

        [ point_index, more_points ] = vec_colex_next3 ( d, order_1d, point_index, more_points );

        if ( ~more_points )
          break
        end

        point_count = point_count + 1;
        point_unique = sparse_unique_index(point_count);
        sparse_order(1:d,point_unique) = order_1d(1:d);
        sparse_index(1:d,point_unique) = point_index(1:d);

      end

      if ( ~more_grids )
        break
      end

    end

  end

  return
end