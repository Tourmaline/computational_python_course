import numpy as np;
from numpy import linalg as la;
import densmatlib as dm; 


n=10;
nocc = 2;
X = dm.rand_symm_matrix(n);
print('Created random symmetrix matrix.')


# iterOutput = {};
# totalOutput = [];
i = 1;

maxit=50;
while i < maxit:
    Xsq = dm.msquare(X);
    
    Xtr = dm.mtrace(X);
    Xsq_tr = dm.mtrace(Xsq);
    
    if abs(Xsq_tr - nocc) < abs(2*Xtr - Xsq_tr - nocc):
        X = Xsq;
        poly = 1;
    else:
        X = 2*X-Xsq;
        poly = 0;
        
        
    stop = 0;
    if dm.mnorm(X,Xsq) < 0.00000001:
        print('Stop iterations')
        stop = 1;
        
    # iterOutput['i'] = i;
    # iterOutput['p'] = poly;
    # 
    # 
    # # totalOutput.append(iterOutput);  list contains a reference to the original dictionary
    # totalOutput.append(iterOutput.copy()); # make a deep copy of a dictionary
    i += 1;
    
    if stop == 1:
        break;
    
    
# print('Done!')
# print('X^2 = \n', Xsq)
# print(totalOutput)

#check_result(Xsq);
