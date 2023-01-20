## This is sample ode Module for Mass Spring Damper System.

def ode(t,x0,param):    # param are parameters, x0 are initial conditions. 
    
    x1_dot = x0[1]
    x2_dot = -(param.c/param.m)*x0[1]-(param.k/param.m)*x0[0]
 
    return([x1_dot,x2_dot])
