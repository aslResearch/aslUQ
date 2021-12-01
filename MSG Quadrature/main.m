clc
clear
close all

% Main file

%% Input the dimensions of uncertain variables.
d = 2;

%% Input the maximum accuracy level. 
L = 4;

%% Input the number of Gaussian random variables.
d_Gaussian = 2;

%% Input the number of Uniform random variables.
d_Uniform = 0;

%% Obtain the nodes and weights of mixed sparse grid quadrature
[nodes, weights] = msg_quadrature(d, L, d_Gaussian, d_Uniform);
