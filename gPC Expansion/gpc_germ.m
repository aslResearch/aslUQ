function xi=gpc_germ(V, n_sample, D)
syschar = V{1};
xi = zeros(n_sample, D);

% written by: Rajnish
for ct=1:D
    if syschar(ct)=='P'
        xi(:, ct) = unifrnd(0,1,n_sample,1);
    elseif syschar(ct)=='H'
        xi(:, ct) = randn(n_sample,1);     
    end
end