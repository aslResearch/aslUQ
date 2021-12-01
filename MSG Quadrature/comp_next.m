function [ a, more, h, t ] = comp_next ( n, k, a, more, h, t )
% This function computes the compositions of the integer N into K parts
% i.e, a composition of the integer N into K parts is an ordered sequence
%    of K nonnegative integers which sum to N

% Inputs: (i) n =  the integer whose compositions are desired.
%         (ii) k = the number of parts in the composition.
%         (iii) a =  the previous composition.  On the first call, set a = []. 
%         (iv) more = boolean. On first call, set more = FALSE.
%

%%
  if ( ~more )

    t = n;
    h = 0;
    a(1) = n;
    a(2:k) = 0;

  else
      
    if ( 1 < t )
      h = 0;
    end

    h = h + 1;
    t = a(h);
    a(h) = 0;
    a(1) = t - 1;
    a(h+1) = a(h+1) + 1;

  end

  more = ( a(k) ~= n );

  return
end