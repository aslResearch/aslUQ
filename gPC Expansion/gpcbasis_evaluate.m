function basis_val=gpcbasis_evaluate(V,xi)
syschar = V{1};
indexes = V{2};
N = size(indexes, 1);
Q = size(xi,1);
D = size(xi,2);
% written by: Rajnish
for ct=1:D
    if syschar(ct)=='P'
        dist(ct).name= 'uniform';
    elseif syschar(ct)=='H'
        dist(ct).name= 'normal';       
    end
end

%% Basis Evaluation FOR the Legendre and hermite Polynomials at xi nodes
for cl=1:N
        dum_val=1;
        for cd=1:D
            ditribution_type = dist(cd);
            if strcmp(ditribution_type.name,'uniform')==1
                basis_eval = legendre_shifted_poly(indexes(cl,cd),xi(:,cd));
            elseif strcmp(ditribution_type.name,'normal')==1
                basis_eval = hermite_poly(indexes(cl,cd),xi(:,cd));
            else
                error('Enter random variables with either Uniform or Gaussian distribution')
            end
            dum_val=dum_val.*basis_eval;
        end
        basis_val(cl,:)=dum_val;
end
return




