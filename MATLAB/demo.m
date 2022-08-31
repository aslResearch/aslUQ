clc
clear
close all

addpath(genpath(pwd))

%% Define parameters for simulation

% System ODE
odefun = @spring_mass_damper;

% Time Vector for integration
dt = 0.1;
tvec = 0:dt:10;

% Input the time instant at which you want the bivariate PDF contour
t_sol = 2;

% Specify the ODE45 Options
opts = [];

% Order of gPC Expansion
P = 4;

% Input the maximum accuracy level. 
L = 7;

% Input the number of samples where you want to evaluate your gPC solution
n_sample = 5000;

%% Normal Distribution
% Specify a vector of mean of the normally distributed random variables
% depending on the number of normally distributed variables
mu = [10; 1]; % mean of x1 and x2 states
    
% Specify a vector of standard deviation of the normally distributed random variables
% depending on the number of normally distributed variables
sigma = [1; 0.1];  %std. deviation of x1 and x2 states


%% Uniform Distribution
% Specify a vector of lower bounds of the uniformly distributed random variables
lb = [8; 18];  % lower bound of m and c
    
% Specify a vector of upper bounds of the uniformly distributed random variables
ub = [12; 22]; % upper bound of m and c


%% Run msgGPC helper function to obtain collocation nodes and gPC parameters
[ x_gaussian, x_uniform, weights, Q, Norm_psi, phi, V] = msgGPC(P, L, mu, sigma, lb, ub);

%% Assign the collocation nodes to appropriate uncertain variables
% Identify the id of the states (size: n) which are uncertain and assign
% the appropriate collocation node
% If any state is deterministic, provide the deterministic value
state.x1 = x_gaussian(1,:);
state.x2 = x_gaussian(2,:);
% state.x3 = 5; % deterministic

% Identify the id of the parameters which are uncertain and assign the
% appropriate collocation node
% If any parameter is deterministic, provide the deterministic value
params.m = x_uniform(1, :);
params.c = x_uniform(2, :);
params.k = 60; % deterministic

%% Obtain the solution of quantities of interest (cell array: 1 x n )
qoi = collocationSIM(odefun, tvec, state, opts, params, Q);

% Extract the collocation solution of all the states from stuct array.
x1_collocation = qoi{1}; 
x2_collocation = qoi{2};

%% Obtain the coefficients of gPC expansion using the following
x1_coefficient = gpc_coefficients(Q, Norm_psi,phi,weights,x1_collocation); 
x2_coefficient = gpc_coefficients(Q, Norm_psi,phi,weights,x2_collocation);

%% Obtain the Mean of quantities y and z using the following
x1_mean = gpc_mean(x1_coefficient);
x2_mean = gpc_mean(x2_coefficient);

%% Obtain the Covariance between y and z using the following
for ct = 1:length(tvec)
    x1_variance(:,ct) = gpc_covariance(Norm_psi, x1_coefficient(:,ct));
    sig3x1(:,ct) = 3*sqrt(x1_variance(:,ct));
    x2_variance(:,ct) = gpc_covariance(Norm_psi, x2_coefficient(:,ct));
    sig3x2(:,ct) = 3*sqrt(x2_variance(:,ct));
end

%% Generate ensemble of gPC expanded solutions
for ct = 1:length(tvec)
    % Compute the time index
    time_index = int32(tvec(ct)/dt+1);
    
    % Obtain the randon germ samples based on distribution of random
    % variables
    xi = gpc_germ(V, n_sample);
    
    % Evaluate gPC at germ samples
    x1_ensemble(ct,:) = gpc_evaluate(x1_coefficient(:,time_index), V, xi);
    x2_ensemble(ct,:) = gpc_evaluate(x2_coefficient(:, time_index), V, xi);
end

%% Plotting
%% Plot the mean and associated 3-sigma confidence bounds
figure(1)
subplot(211)
plot(tvec, x1_mean, 'r-', 'linewidth', 1.2);
hold on
plot(tvec, x1_mean+sig3x1, 'k--', 'linewidth', 1.2);
plot(tvec, x1_mean-sig3x1, 'k--', 'linewidth', 1.2);
legend('Mean', 'Mean+3\sigma', 'Mean-3\sigma');
xlabel('Time');
ylabel('Position in m');

subplot(212)
plot(tvec, x2_mean, 'r-', 'linewidth', 1.2);
hold on
plot(tvec, x2_mean+sig3x2, 'k--', 'linewidth', 1.2);
plot(tvec, x2_mean-sig3x2, 'k--', 'linewidth', 1.2);
legend('Mean', 'Mean+3\sigma', 'Mean-3\sigma');
xlabel('Time');
ylabel('Velocity in m/s');

%% Plot the contour plot of bivariate probability density function
figure(2)
% Compute the time index where the solution is desired
time_ind = int32(t_sol/dt+1);
dscatter(x1_ensemble(time_ind,:)', x2_ensemble(time_ind,:)', 'PLOTTYPE','contour');
xlabel('Position in m');
ylabel('Velocity in m/s');
