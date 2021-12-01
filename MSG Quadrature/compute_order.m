function order = compute_order(d, q, vec_rules)
%% Compute the order of polynomials based on accuracy level (q)
order = zeros(d, 1);

for ind_dim = 1:d
    if ( vec_rules(ind_dim) == 1 )
        if ( q(ind_dim) == 0 )
            order(ind_dim) = 1; % order is 1 if accuracy level is 0
        else
            order(ind_dim) = kpn_order(q(ind_dim)); % use function kpn_order for other accuracy levels
        end
    elseif ( vec_rules(ind_dim) == 2 )
        if ( q(ind_dim) == 0 )
            order(ind_dim) = 1; % order is 1 if accuracy level is 0
        else
            order(ind_dim) = kpu_order(q(ind_dim)); % use function kpn_order for other accuracy levels
        end
    end
end
end