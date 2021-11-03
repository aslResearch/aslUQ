function covv=gpc_covariance(nrm2,a_i_alpha, b_j_alpha)

% if B is not specified we compute the (auto-) covariance of A
if nargin<3 || isempty(b_j_alpha)
    b_j_alpha = a_i_alpha;
end

% compute weighted inner product between A and B giving the covariance 

covv = a_i_alpha(:,2:end)*diag(nrm2(2:end))*b_j_alpha(:,2:end)';

