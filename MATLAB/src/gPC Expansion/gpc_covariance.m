function cov = gpc_covariance(Norm_psi,x_c, y_c)
% gpc_covariance: This function computes covariance between two random
%                 processes (x and y), given the coefficients of gPC 
%                 expansion (x_c and y_c) of both x and y.
%                 Instead, if y_c is not provided or empty, the function 
%                 computes the auto-covariance of random process x.
%
% Inputs:
%       (i) Norm_psi = gPC Normalization coefficients (1 x N array)
%       (ii) x_c = gPC coefficients of random process x (1 x N array)
%       (iii) y_c = gPC coefficients of random process y (1 x N array)
%
% Output:
%        cov = covariance between x and y if nargin=3 (2 x 2 array), autocovariance of x
%              if nargin = 2 (scalar)

%% Covariance calculation

% Covariance is computed as a normalization weighted inner product between
% 2nd to Nth order gPC coefficients (excluding the zeroth order)

% if y_c is not specified, equate y_c to x_c to compute autocovariance of x
if nargin<3 || isempty(y_c)
    y_c = x_c;
end

% If x_c or y_c is row vector, convert it into column vector;
if iscolumn(x_c)
    x_c = x_c';
end

if iscolumn(y_c)
    y_c = y_c';
end

% Extract 2nd to Nth order gPC coefficients (excluding the zeroth order)
x_c_req = x_c(:,2:end);
y_c_req = y_c(:,2:end);

% Diagonal Normalization matrix (N-1 x N-1 array)
Gamma_req = diag(Norm_psi(2:end));

% Weighted inner product 
cov = x_c_req*Gamma_req*y_c_req';


