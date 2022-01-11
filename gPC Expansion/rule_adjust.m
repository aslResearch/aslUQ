function [ x, w ] = rule_adjust(a, b, c, d, n, x, w)
% This function takes the uniformly distributed quadrature nodes with the
% PDF between ranges a and b and transforms it to collocation nodes with
% the PDF between ranges c and d.
%

%% Rule Adjustment
  for i = 1 : n
    x(i) = ( ( b - x(i)) * c + (x(i) - a ) * d )/ (b-a);
  end

  s = ( d - c ) / ( b - a );

  w(1:n) = s * w(1:n);

  return;
end