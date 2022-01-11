import numpy as np
def gpc_germ(V, n_sample, D):
    syschar = V[0]
    xi=np.zeros([n_sample,D],int)

    for ct in range(0,D):
        if syschar[ct]== "P":
            xi[:,ct]=np.transpose(np.array([np.random.uniform(0,1,n_sample)]))
        elif syschar[ct]== "H":
            xi[:,ct]=np.transpose(np.array([np.random.normal(0,1,n_sample)]))

    return(xi)

