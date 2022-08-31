function x = gaussian_transformation(mu_vec, sig_vec, nodes, d_Gaussian)
% gaussian_transformation: This function takes the normally distributed standard quadrature nodes with the
% mean vector of zeros and Covariance matrix of identity and transforms it to collocation nodes with
% the PDF N(mu_vec, Sigma) where mu_vec is the vector of mean and Sigma is a
% diagonal matrix of Variance, Sigma = diag(sig_vec.^2)
%
% Inputs:
%       (i) mu_vec = vector of mean of uncertain variables
%       (ii) sig_vec = vector of standard deviation of uncertain variables
%       (iii) nodes = Quadrature Grid obtained directly from quadrature
%                technique (N_q x d array), where N_q is the grid size and
%                d is the total number of uncertain variables
%       (iv) d_Gaussian = number of Gaussian random variables
%       

% If mu is row vector, convert it into column vector;
if isrow(mu_vec)
    mu_vec = mu_vec';
end

xi_Gaussian = nodes(:,1:d_Gaussian)';

x = mu_vec + diag(sig_vec)*xi_Gaussian;


