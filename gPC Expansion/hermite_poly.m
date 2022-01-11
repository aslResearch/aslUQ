function h = hermite_poly(n,x)
% HERMITE:  compute the probabilist Hermite polynomials of degree n.
%           x optional values where we want to evaluate the hermite
%           polynomial of degree n
% call the hermite recursive function.
h = hermite_rec(n);

% evaluate the hermite polynomial function, given x
if( nargin==2 )
    y = h(end) * ones(size(x));
    j = 1;
    for i=length(h)-1:-1:1
        y = y + h(i) * x.^j;
        j = j+1;
    end
    % restore the shape of y, the same as x
    h = reshape(y,size(x));
end


function h = hermite_rec(n)
% This is the reccurence construction of the probabilist Hermite polynomial, i.e.:
%   He_0(x) = 1
%   He_1(x) = x
%   He_[n+1](x) = x He_n(x) - n He_[n-1](x)

% 0th case
if( 0==n ), h = 1;
% 1st case
elseif( 1==n ), h = [1 0];
% n>1
else
    % He_[n-1](x)
    h1 = zeros(1,n+1);
    h1(1:n) = hermite_rec(n-1);
    % He_[n-2](x)
    h2 = zeros(1,n+1);
    h2(3:end) = (n-1)*hermite_rec(n-2);
    % He_[n](x)
    h = h1 - h2;
    
end