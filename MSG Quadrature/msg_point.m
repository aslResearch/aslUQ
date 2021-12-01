function sparse_point = msg_point(d, L, vec_rules, point_num, sparse_order, sparse_index )
% This function computes the points of a sparse grid rule.
%   Inputs: (i) POINT_NUM= the number of unique points in the grid.
%            (ii) SPARSE_UNIQUE_INDEX= index of each point in each of the 1D rules in the grid that generated it.
%           (iii) d = dimension of uncertainty
%           (iv) L = accuracy level
%            (v) vec_rules= vector of 1D rules
%   Output: sparse points


%%  Compute the point coordinates.
%
  sparse_point = zeros ( d, point_num );
  sparse_point(1:d,1:point_num) = 1.0E+30; % assign huge number

  for dim = 1 : d

    for level = 0 : L

      order = compute_order( 1, level, vec_rules(dim) );

      if ( vec_rules(dim) == 1 )
        points = KPN_compute_points ( level );
      elseif ( vec_rules(dim) == 2 )
        points = KPU_compute_points ( level );
      end

      index = find ( sparse_order(dim,1:point_num) == order );

      sparse_point(dim,index) = points ( sparse_index(dim,index) );

    end

  end

  return
end
