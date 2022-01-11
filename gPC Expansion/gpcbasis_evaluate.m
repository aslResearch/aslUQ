function phi=gpcbasis_evaluate(V,xi)
% This function computes the basis of gPC expansion at quadrature nodes
%
% Inputs:
%       (i) V = Cell array with two cells (1 and 2). 
%               Cell 1 contains 'syschar', a string of characters representing orthogonal
%                       polynomials ('H' for Hermite, 'P' for Legendre)
%               Cell 2 contains 'indexes', multi-dinsional indexing (D x N array)
%               D: total number of uncertain variables 
%               N: order of gPC expansion (singly-indexed) obtained from
%                  lexicographic ordering        
%       (ii) xi = Quadrature Grid obtained directly from quadrature
%                  technique (N_q x D array), where N_q is the grid size
%
% Input Example:
% For problem with 4 uncertain variables (2 Gaussian and 2 uniform) and 4th
% order gPC expansion
% P = 4, D = 4, syschar = 'HHPP', N = nchoosek(P+D,P) = 70
% V{1} = 'HHPP'
% V{2} = indexes (70 x 4 array)
% xi = nodes obtained from appropriate quadrature technique (mixed sparse
% grid-based quadrature). For accuracy level of 6, N_q = 181, size of xi = 181 x 4

% Outputs:
%       phi = basis of gPC expansion at quadrature nodes (N x N_q array)

%% Extract the essentials from the input
syschar = V{1};
indexes = V{2};
N = size(indexes, 1);
N_q = size(xi,1);
D = size(xi,2);

%% Extract the polynomial type and create a 'dist' structure with field 'name'
for ct=1:D
    if syschar(ct)=='P'
        dist(ct).name= 'uniform';
    elseif syschar(ct)=='H'
        dist(ct).name= 'normal';       
    end
end

%% Basis Evaluation for the Legendre and hermite Polynomials at xi nodes
% Buffer for basis functions
phi = zeros(N, N_q);

% Outer loop for each polynomial order
for cl=1:N
        phi_1d=1;
        % Inner loop for each dimension of uncertainty type
        for cd=1:D
            % Extract the distribution type (string 'uniform' or 'normal')
            ditribution_type = dist(cd);
            
            % Compare the string of distribution type
            if strcmp(ditribution_type.name,'uniform')==1
                basis_eval = legendre_shifted_poly(indexes(cl,cd),xi(:,cd));
            elseif strcmp(ditribution_type.name,'normal')==1
                basis_eval = hermite_poly(indexes(cl,cd),xi(:,cd));
            else
                error('Enter random variables with either Uniform or Gaussian distribution')
            end
            
            % basis function is the multidimensional product.
            phi_1d=phi_1d.*basis_eval;
        end
        phi(cl,:)=phi_1d;
end
return




