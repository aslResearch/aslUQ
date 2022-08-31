function xd = spring_mass_damper(t, state, params)
% Extract the state
x1 = state(1);
x2 = state(2);

% Extract the parameters
m = params(1);
c = params(2);
k = params(3);

% System of differential equation
x1d = x2;
x2d = -(c/m)*x2-(k/m)*x1;
xd = [x1d;x2d];