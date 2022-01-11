function [N, Norm_psi, V, phi] = gpc_essentials(P, d_Gaussian, d_Uniform, D, xi)
% This function computes the essential parameters of the gPC expansion
% Inputs:
%       (i) P = order of gPC expansion
%       (ii) d_Gaussian = number of Gaussian random variables
%       (iii) d_Uniform = number of uniform random variables
%       (iv) D = total number of uncertain variables
%       (v) xi = Quadrature Grid obtained directly from quadrature
%                technique (N_q x D array), where N_q is the grid size
%
% Input Example:
% For problem with 4 uncertain variables (2 Gaussian and 2 uniform) and 4th
% order gPC expansion
% P = 4, d_Gaussian = 2, d_Uniform = 2, D = 4, syschar = 'HHPP'
% xi = nodes obtained from appropriate quadrature technique (mixed sparse
% grid-based quadrature). For accuracy level of 6, N_q = 181, size of xi = 181 x 4

% Outputs:
%       (i) N = order of gPC expansion (singly-indexed) obtained from
%                lexicographic ordering = nchoosek(P+D,P) 
%       (ii) Norm_psi = vector of normalization coefficients (1 x N array)
%       (iii) V = Cell array with two cells (1 and 2). 
%               Cell 1 contains 'syschar', a string of characters representing orthogonal
%                       polynomials ('H' for Hermite, 'P' for Legendre)
%               Cell 2 contains 'indexes', multi-dinsional indexing (D x N array)
%               D: total number of uncertain variables 
%               N: order of gPC expansion (singly-indexed) obtained from
%                  lexicographic ordering     
%       (iv) phi = basis of gPC expansion at quadrature nodes (N x N_q array)

%% Generate contiguous strings of 'H' and 'P' depending on the number of Gaussian and uniform random variables.
% string of characters representing orthogonal polynomials ('H' for Hermite, 'P' for Legendre)

sys_string_g =join(string(repmat('H',1,d_Gaussian)),''); %% sys_string_g = 'HH'
sys_string_u =join(string(repmat('P',1,d_Uniform)),''); %% sys_string_u = 'PP'

% Join the two strings to obtain one single combined string of "H" and "P"
sys_string = strcat(sys_string_g, sys_string_u); %% sys_string = "HHPP"

% Convert the string sys_string to characters without quotes
syschar = convertStringsToChars(sys_string); %% syschar = HHPP (without quotes)

%% gPC norm, order and indexes
[Norm_psi, N, indexes]=multi_index(P,D,syschar); % N = 70
V = {syschar,indexes};  %combine rules in sychar and indexes as one struct variable

%% evaluate the basis functions at collocation nodes
phi = gpcbasis_evaluate(V,xi); 
return;