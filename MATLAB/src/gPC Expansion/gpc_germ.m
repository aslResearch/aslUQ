function xi=gpc_germ(V, n_sample)
% gpc_germ computes samples for evaluating gPC expansion of a stochastic
% process.
% Inputs:
%       (i) V = Cell array with two cells (1 and 2). 
%               Cell 1 contains 'syschar', a string of characters representing orthogonal
%                       polynomials ('H' for Hermite, 'P' for Legendre)
%               Cell 2 contains 'indexes', multi-dinsional indexing (D x N array)
%               D: total number of uncertain variables 
%       (ii) n_sample = number of samples required
% Input Example:
% For problem with 4 uncertain variables (2 Gaussian and 2 uniform) and 4th
% order gPC expansion
% P = 4, D = 4, syschar = 'HHPP', N = nchoosek(P+D,P) = 70
% V{1} = 'HHPP'
% V{2} = indexes (70 x 4 array)

% Outputs:
%       xi = Random sample points within standard distribution


%% Extract the essentials

syschar = V{1};
nodes_sg = V{2};
D = size(nodes_sg, 2);
xi = zeros(n_sample, D);

% written by: Rajnish
for ct=1:D
    if syschar(ct)=='P'
        xi(:, ct) = lhsdesign(n_sample,1);
    elseif syschar(ct)=='H'
        xi(:, ct) = randn(n_sample,1);     
    end
end