function [ x_gaussian, x_uniform, weights, Q, Norm_psi, phi, V] = msgGPC(P, L, mu, sigma, lb, ub)
% msgGPC: Helper function to obtain nodes and weights from Mixed Sparse
% Grid Quadrature technique. msgGPC also outputs the essential parameters
% of the generalized polynomial chaos expansion order.
% 
% Inputs:
% (i)   P = order of gPC expansion
% (ii)  L = desired accuracy level of MSG quadrature
% (iii) mu = vector of mean of normally distributed uncertain variables
%           (d_Gaussian x 1 array)
% (iv) sigma = vector of standard deviation of normally distributed
%              uncertain variables (d_Gaussian x 1 array)
% (v)  lb = vector of lower bounds of uniformly distributed uncertain
%           variables (d_Uniform x 1 array)
% (vi) ub = vector of upper bounds of uniformly distributed uncertain
%           variables (d_gaussian x 1 array)
% (vii) V = Cell array with two cells (1 and 2). 
%               Cell 1 contains 'syschar', a string of characters representing orthogonal
%                       polynomials ('H' for Hermite, 'P' for Legendre)
%               Cell 2 contains 'indexes', multi-dinsional indexing (D x N array)
%               D: total number of uncertain variables 
%               N: order of gPC expansion (singly-indexed) obtained from
%                  lexicographic ordering     
%
% Outputs:
% (i) x_gaussian = collocation nodes with the PDF N(mu, sigma.^2) of size
%                  (d_Gaussian x Q array)
% (ii) x_uniform = uniformly distributed collocation nodes with the PDF
%                  U[lb, up] of size (d_Uniform x Q array).
% (iii) weights = Weights of mixed sparse grid rule (1 X Q array)
% (iv) Q = total number of collocation nodes for all uncertain variables
% (v) Norm_psi = vector of normalization coefficients (1 x N array)
% (vi) phi = basis of gPC expansion at quadrature nodes (N x Q array) where
%            N is the order of gPC expansion (singly-indexed) obtained from
%            reverse-graded lexicographic ordering = binom(d, P)    


%% Convert inputs to appropriate sizes
% If mu is row vector, convert it into column vector;
if isrow(mu)
    mu = mu';
end

% If sigma is row vector, convert it into column vector;
if isrow(sigma)
    sigma = sigma';
end

% If lb is row vector, convert it into column vector;
if isrow(lb)
    lb = lb';
end

% If ub is row vector, convert it into column vector;
if isrow(ub)
    ub = ub';
end

%% Compute the number of Gaussian and Uniform uncertain variables
d_Gaussian = size(mu, 1);
d_Uniform = size(lb, 1);

% Compute the total number of uncertain variables
d = d_Gaussian + d_Uniform;

%% Obtain the nodes and weights from mixed sparse grid quadrature
[nodes, weights] = msg_quadrature(d, L, d_Gaussian, d_Uniform);

% Total sample size
Q = length(weights);

fprintf('\n');
fprintf('==========  Generated MSG Nodes and Weights  ==========');
fprintf('\n');
fprintf(' Number of MSG Nodes generated = %d', Q);
fprintf('\n');


%% Essentials of gPC expansion
[N, Norm_psi,V, phi] = gpc_essentials(P, d_Gaussian, d_Uniform, d, nodes); 

fprintf('\n');
fprintf('=======  Generated essentials of gPC expansion  =======');
fprintf('\n');

%% Transform the quadrature nodes to the collocation nodes with appropriate PDF

% Gaussian Transformation to the Input PDF
if d_Gaussian    
    % Obtained Random Vector within the Desired Normal PDF
    x_gaussian = gaussian_transformation(mu, sigma, nodes, d_Gaussian);
else
    x_gaussian = [];
end

% Uniform Transformation to the Input PDF
if d_Uniform 
    % Obtained Random Vector within the Desired Uniform PDF
    x_uniform = uniform_transformation(lb, ub, nodes, d, d_Uniform);
else
    x_uniform = [];
end








