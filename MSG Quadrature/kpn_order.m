function n = kpn_order ( l )
% This function computes the order of a KPU rule from the level.
% Inputs: L=  accuracy level of the rule (1 <= L <= 25)

%%
  if ( l < 1 )
    fprintf ( 1, '\n' );
    fprintf ( 1, 'KPN_ORDER - Fatal error!\n' );
    fprintf ( 1, '  1 <= L <= 25 required.\n' );
    fprintf ( 1, '  Input L = %d\n', l );
    error ( 'KPN_ORDER - Fatal error!' );
  elseif ( l == 1 )
    n = 1;
  elseif ( l <= 3 )
    n = 3;
  elseif ( l == 4 )
    n = 7;
  elseif ( l <= 8 )
    n = 9;
  elseif ( l == 9 )
    n = 17;
  elseif ( l <= 15 )
    n = 19;
  elseif ( l == 16 )
    n = 31;
  elseif ( l == 17 )
    n = 33;
  elseif ( l <= 25 )
    n = 35;
  else
    fprintf ( 1, '\n' );
    fprintf ( 1, 'KPN_ORDER - Fatal error!\n' );
    fprintf ( 1, '  1 <= L <= 25 required.\n' );
    fprintf ( 1, '  Input L = %d\n', l );
    error ( 'KPN_ORDER - Fatal error!' );
  end

  return
end
