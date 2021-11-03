function gpc_coeff = gpc_coefficients_cal(Norm_psi,phi,w,x)
%% gPC coefficients calculation
sum_all_x1 = x*(phi'.*w);
gpc_coeff = (1./Norm_psi).*sum_all_x1;
gpc_coeff = gpc_coeff';