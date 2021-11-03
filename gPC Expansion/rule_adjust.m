function [ x, w ] = rule_adjust ( a, b, c, d, n, x, w )
  for i = 1 : n
    x(i) = ( ( b - x(i)) * c + (x(i) - a ) * d )/ ( b- a );
  end

  s = ( d - c ) / ( b - a );

  w(1:n) = s * w(1:n);

  return;
end