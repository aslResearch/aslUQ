function x_c = gpc_coefficients(Q, Norm_psi,phi,w,x)
% gpc_coefficients: This function computes the coefficients of gPC expansion for the solution of the variables
% at the collocation nodes.
%
% Inputs:
%       (i) Norm_psi = gPC Normalization coefficients (1 x N array)
%       (ii) phi = array of gPC basis evaluated at quadrature nodes 
%                  (N x Q array) where Q is the number of quadrature nodes
%       (iii) w = array of collocation weights (Q x 1 array)
%       (iv) x = solution of vector x at collocation nodes (n x Q
%                array), where n is the dimension of vector x.
%
% Output:
%        x_c = array of gPC coefficients of the variable x (N X N_x)

% Obtain x of appropriate size
if size(x, 2)~=Q
    x = x';
end

%% gPC coefficients calculation
% Diagonal Normalization matrix (N x N array)
Gamma = diag(Norm_psi);

% Diagonal Collocation Weight Matrices (N_q x N_q array)
W = diag(w);

% gPC coefficient of the variable x
x_c = inv(Gamma)*phi*W*x';
