function qoi = collocationSIM(odefun, tspan, state, opts, params, Q)
% collocationSIM: integrates the system of differential equations:
% state'= f(t,state,params) from time t0 to tfinal at the
% collocation nodes of uncertain and deterministic variables. 
%
% Inputs:
% (i) odefun =  function handle of the differential equation 
%               state'= f(t,state,params). The individual state variables
%               and the parameters of the differential equation must be
%               extracted (in odefun) in the order they were passed into 
%               state and params
% (ii) tspan = integration time vector =[t0 tfinal]
% (iii) state = struct with the fields (n fields for n-dimensional system)
%               representing the collocation nodes of state variables at 
%               initial time t0
% (iv) opts = Options for ODE45. See ODESET for details.
% (v) params = struct with the fields representing the collocation nodes
%               of parameters 
% (vi) Q = total number of collocation nodes for all uncertain variables
%
% Output:
%       qoi = solution of quantities of interest (cell array: 1 x n ) and
%             the collocation solution of each state variable can be
%             extracted from qoi. For e.g. x1 = qoi{1}, x2 = qoi{2}.

stateCell = struct2cell(state);
paramCell = struct2cell(params);

x0 = zeros(size(stateCell,1), Q);
parameters = zeros(size(paramCell,1), Q);
for cc = 1:Q
    for cf = 1:size(stateCell,1)
        if size(stateCell{cf},2)~=1
            x0(cf,cc) = stateCell{cf}(cc); 
        else
            x0(cf,cc) = stateCell{cf}(1);
        end
    end
    
    for cf = 1:size(paramCell,1)
        if size(paramCell{cf},2)~=1
            parameters(cf, cc) = paramCell{cf}(cc);
        else
            parameters(cf, cc) = paramCell{cf}(1);
        end
    end
end

for cc = 1:Q
    [~, xst] = ode45(odefun, tspan, x0(:, cc), opts, parameters);
    for cf = 1:size(stateCell,1)
        qoi{cf}(:,cc) = xst(:,cf);
    end
end

fprintf('\n');
fprintf('=========  Collocation Simulation Completed  ==========');
fprintf('\n');