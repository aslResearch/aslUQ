Highlight:
    This repository carries out quantification and propagation of uncertainties in stochastic dynamical systems using Generalized Polynomial Chaos Expansion. 

Methodology:
    The toolbox uses Mixed Sparse Grid quadrature nodes and weights to carry out pseudospectral collocation-based gPC expansion. 

Use:
    For any stochastic process, the toolbox can compute the mean, variance, covariance, solution ensembles, contour bi-variate probability density function.

Applicable to:
    Dynamical Models with Gaussian and Uniform Distribution of Uncertainties

Programming Languages:
    MATLAB and Python


Windows

    1. Clone this github repo
        cd ~
        git clone https://github.com/aslResearch/aslUQ
    2. Edit the Uncertainty Quantification/MATLAB/demo.m to include the desired simulation parameters
    3. Add the ode45 model .m file in Quantification/MATLAB/: 
        The example ode45 model .m file for the demo is "spring_mass_damper.m"
    * The Uncertainty Quantification/MATLAB/src contains the MATLAB source files to carry out gPC expansion. 
