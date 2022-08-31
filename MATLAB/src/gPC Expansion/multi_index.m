function[Norm_psi, N, indexes]=multi_index(P,D,syschar)
% This function computes the normalization coefficients, total
% multi-dimensional order of gPC expansion, and reverse-graded lexocgraphic
% indexing of gPC orders in each dimension of uncertainty
%
% Inputs:
%       (i) P = order of gPC expansion
%       (ii) D = total number of uncertain variables
%       (iii) syschar = string of characters representing orthogonal
%                       polynomials ('H' for Hermite, 'P' for Legendre)
%
% Input Example:
% For problem with 4 uncertain variables (2 Gaussian and 2 uniform) and 4th
% order gPC expansion
% P = 4, D = 4, syschar = 'HHPP'

% Outputs:
%       (i) N = order of gPC expansion (singly-indexed) obtained from
%                lexicographic ordering = nchoosek(P+D,P) 
%       (ii) Norm_psi = vector of normalization coefficients (1 x N array)
%       (iii) indexes = multi-dinsional indexing (N x D array)

%% Extract the polynomial type and create a 'dist' structure with field 'name'
for ct=1:D
    if syschar(ct)=='P'
        dist(ct).name= 'uniform';
    elseif syschar(ct)=='H'
        dist(ct).name= 'normal';       
    end
end

% Check if the number of 'name' fields in 'dist' structure is equal to the dimension of
% uncertainty
if D ~= length(dist)
   error('Dimension Mismatch');
end

%% Compute indexes and order
[indexes,N] = Indexes(P,D);

%% Normalization coefficients for the Legendre and hermite Polynomials

% One Dimensional Normalization Constants
norm_legendre=@(n) 1./(2*n+1);  
norm_hermite= @(n) factorial(n);

% Buffer for multi-dimensional normalization constants
Norm_psi=ones(1,N);

% Outer loop for each polynomial order
for l=1:N
    % Inner loop for each dimension of uncertainty type
    for cd=1:D
        % Extract the distribution type (string 'uniform' or 'normal')
        ditribution_type = dist(cd); 
        
        % Compare the string of distribution type
        if strcmp(ditribution_type.name,'uniform')==1
            normalization_coeff = norm_legendre((indexes(l,cd)));
        elseif strcmp(ditribution_type.name,'normal')==1
            normalization_coeff = norm_hermite((indexes(l,cd)));
        else
            error('Enter random variables with either Uniform or Gaussian distribution')
        end
        
        % Normalization constant is the multidimensional product.
        Norm_psi(l)=Norm_psi(l)*normalization_coeff;
    end
end
return




