function [point_index, rep] = vec_colex_mine(dim_num, base, point_index, rep)

%*****************************************************************************80
%
%% VEC_COLEX_NEXT3 generates vectors in colex order.
%
%  Discussion:
%
%    The vectors are produced in colexical order, starting with
%    (1,1,...,1),
%    (2,1,...,1),
%    ...
%    (BASE(1),BASE(2),...,BASE(DIM_NUM)).
%
%  Example:
%
%    DIM_NUM = 2, 
%    BASE = [ 3, 3]
%
%    1   1
%    2   1
%    3   1
%    1   2
%    2   2
%    3   2
%    1   3
%    2   3
%    3   3
%
%  Licensing:
%
%    This code is distributed under the GNU LGPL license.
%
%  Modified:
%
%    19 August 2008
%
%  Author:
%
%    John Burkardt
%
%  Reference:
%
%    Dennis Stanton, Dennis White,
%    Constructive Combinatorics,
%    Springer, 1986,
%    ISBN: 0387963472,
%    LC: QA164.S79.
%
%  Parameters:
%
%    Input, integer DIM_NUM, the spatial dimension.
%
%    Input, integer BASE(DIM_NUM), the base to be used in each dimension.
%
%    Input, integer A(DIM_NUM), except on the first call, this should
%    be the output value of A on the last call.
%
%    Input, logical MORE, should be FALSE on the first call, and
%    thereafter should be the output value of MORE from the previous call.  
%
%    Output, integer A(DIM_NUM), the next vector.
%
%    Output, logical MORE, is TRUE if another vector was computed.
%    If MORE is FALSE on return, then ignore the output value A, and
%    stop calling the routine.
%

if rep==0
    point_index(1:dim_num) = 1;
    rep = 1;
else
    for i = 1:dim_num
        point_index(i) = point_index(i)+1;
        if (point_index(i) <= base(i) )
            return
        end
        point_index(i) = 1;
    end
    rep=0;
end
    
    
%   if ( ~more )
% 
%     a(1:dim_num) = 1;
%     more = 1;
% 
%   else
%       
%     for i = 1 : dim_num
% 
%       a(i) = a(i) + 1;
% 
%       if ( a(i) <= base(i) )
%         return
%       end
% 
%       a(i) = 1;
% 
%     end
% 
%     more = 0;
% 
%   end

  return
end