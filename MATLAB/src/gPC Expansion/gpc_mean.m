function mean_x = gpc_mean(x_c)
% gpc_mean: This function computes the mean of the random process vector x
%           given the coefficients of gPC expansion x_c.
%
% Input: (i)  x_c = gPC coefficients of random process x (1 x N array)
%
% Outputs:
%       (i) mean_x = mean of the random process x           

% Obtain the zeroth order coefficient as the mean
mean_x = x_c(1,:);
