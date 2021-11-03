function a_i_j=gpc_evaluate( a_i_alpha, V, xi )
% check whether arguments a_i_alpha, I_a and xi match
% evaluate the gpc basis functions
y_alpha_j = gpcbasis_evaluate(V,xi);

% multiply with gpc coefficients
% N x k : (N x M) * (M x k)
a_i_j = a_i_alpha' * y_alpha_j;
