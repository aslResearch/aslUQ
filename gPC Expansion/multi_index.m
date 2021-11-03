function[Norm_psi, N, indexes]=multi_index(P,D,syschar)
for ct=1:D
    if syschar(ct)=='P'
        dist(ct).name= 'uniform';
    elseif syschar(ct)=='H'
        dist(ct).name= 'normal';       
    end
end

if D ~= length(dist)
   error('Dimension Mismatch');
end

[indexes,N] = Indexes(P,D);
%% NORM FOR the Legendre and hermite Polynomials
norm_legendre=@(n) 1./(2*n+1);  
norm_hermite= @(n) factorial(n);
% norm_hermite= @(n) sqrt(pi)*(2^n)*factorial(n);
% Norm_psi=zeros(1,N);
Norm_psi=ones(1,N);
for l=1:N
    for cd=1:D
        ditribution_type = dist(cd); 
        if strcmp(ditribution_type.name,'uniform')==1
            normalization_coeff = norm_legendre((indexes(l,cd)));
        elseif strcmp(ditribution_type.name,'normal')==1
            normalization_coeff = norm_hermite((indexes(l,cd)));
        else
            error('Enter random variables with either Uniform or Gaussian distribution')
        end
        Norm_psi(l)=Norm_psi(l)*normalization_coeff;
    end
end
return




