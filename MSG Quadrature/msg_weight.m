function sparse_weight = msg_weight (d, L, vec_rules, point_num, sparse_unique_index )
% This function computes sparse grid weights based on a mixture of 1D rules.
%   Inputs: (i) POINT_NUM= the number of unique points in the grid.
%            (ii) SPARSE_UNIQUE_INDEX= index of each point in each of the 1D rules in the grid that generated it.
%           (iii) d = dimension of uncertainty
%           (iv) L = accuracy level
%            (v) vec_rules= vector of 1D rules
%   Output: sparse weights

%%
  sparse_weight(1:point_num) = 0.0;

  point_total = 0;

  level_min = max ( 0, L + 1 - d );

  for level = level_min : L
%
%  The middle loop generates the next partition LEVEL_1D(1:DIM_NUM)
%  that adds up to LEVEL.
%
    level_1d = [];
    more_grids = 0;
    h = 0;
    t = 0;

    while ( 1 )     

    [ level_1d, more_grids, h, t ] = comp_next(level, d, level_1d, more_grids, h, t );
%
%  Transform each 1D level to a corresponding 1D order.
%
      order_1d = compute_order( d, level_1d, vec_rules );
%
%  The product of the 1D orders gives us the number of points in this grid.
%
      order_nd = prod ( order_1d(1:d) );
%
%  Compute the weights for this grid.
%
%  The correct transfer of data from the product grid to the sparse grid
%  depends on the fact that the product rule weights are stored under colex
%  order of the points, and this is the same ordering implicitly used in
%  generating the SPARSE_UNIQUE_INDEX array.
%
      grid_weight = msg_product_weight(d, level_1d, order_1d, order_nd, vec_rules);
%
%  Compute Smolyak's binomial coefficient for this grid.
% See Jia, Xen, and Cheng Paper: Eqn. (26)
      coeff = (-1)^( L - level)* nchoosek( d - 1, L - level);
%
%  Add these weights to the rule.
%
      for order = 1 : order_nd

        point_total = point_total + 1;

        point_unique = sparse_unique_index(point_total);

        sparse_weight(point_unique) = sparse_weight(point_unique)+coeff * grid_weight(order);

      end

      if ( ~more_grids )
        break
      end

    end

  end

  return
end