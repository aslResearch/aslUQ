function x = uniform_transformation(lower, upper, nodes, d, d_Uniform)
% uniform_transformation: This function takes the uniformly distributed standard quadrature nodes with the
% PDF between ranges 0 and 1 and transforms it to uniformly distributed collocation nodes with
% the PDF between ranges-lower and upper.
%
% Inputs:
%       (i) lower = vector of lower bounds of uniformly distributed uncertain variables
%       (ii)upper = vector of upper bounds of uniformly distributed uncertain variables
%       (iii) nodes = Quadrature Grid obtained directly from quadrature
%                technique (N_q x d array), where N_q is the grid size and
%                d is the total number of uncertain variables
%       (iv) d_Uniform = number of Uniform random variables
%  

Q = size(nodes, 1);
d_Gaussian = d-d_Uniform;
xi_Uniform = nodes(:,d_Gaussian+1:d_Gaussian+d_Uniform);
b = 1;
a = 0;
b_mat = b*ones(Q, d_Uniform);
a_mat = a*ones(Q, d_Uniform);

x = (b_mat-xi_Uniform)*diag(lower)+(xi_Uniform-a_mat)*diag(upper);
x = x';

