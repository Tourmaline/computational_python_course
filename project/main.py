import numpy as np;
from numpy import linalg as la;
import densmatlib as dm; 

n=10;
nocc = 5;
X = dm.rand_symm_matrix(n);
print('Created random symmetrix matrix.')


iterOutput = {};
totalOutput = [];
i = 1;

Xsq = dm.msquare(X);

maxit=100;
while i < maxit:
    Xtr = dm.mtrace(X);
    Xsq_tr = dm.mtrace(Xsq);
    
    if abs(Xsq_tr - nocc) < abs(2*Xtr - Xsq_tr - nocc):
        X = Xsq;
        poly = 1;
    else:
        X = 2*X-Xsq;
        poly = 0;
        
    Xsq = dm.msquare(X);
        
    stop = 0;
    normXmXsq = dm.mnorm(X,Xsq);
    if normXmXsq < 0.00000001:
        print('Stop iterations: i = {}'.format(i))
        stop = 1;
        
    iterOutput['i'] = i;
    iterOutput['p'] = poly;
    iterOutput['idemp_err'] = normXmXsq; 
    
    totalOutput.append(iterOutput.copy()); # make a deep copy of a dictionary
    i += 1;
    
    if stop == 1:
        break;
    
    
print('Done!')
print('Trace of the density matrix is {}'.format(dm.mtrace(X)))

# extract error
err = [];
for val in totalOutput:
    err.append(val['idemp_err']);

import matplotlib.pyplot as plt
plt.semilogy(err, 'r*-')
plt.xlabel('Iteration')
plt.ylabel('Idempotency error')
plt.grid(True)
plt.show()
