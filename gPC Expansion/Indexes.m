function [indexes,N] = Indexes(P,D)
% This function creates a vector of indexes for the degrees of the different 
% orthogonal polynomials.

%      P  maximum value inside indexes (i.e maximum degree for a specific
%           direction)
%      D    Stochastic dimension of the problem

N       = nchoosek(P+D,P); 
indexes = zeros(N,D);
v       = ones(1,D);
for s = 1:N   
  indexes(s, 1:D-1) = -diff(v);
  indexes(s, D)     = v(D) - 1;
    %% Update index vector:
    for k = D:-1:1
      v(k) = v(k) + 1;
      if k > 1
        if v(k) <= v(k - 1)
          break;  % Exit for k loop
        end
        v(k) = 1;
      end
    end
end


end
