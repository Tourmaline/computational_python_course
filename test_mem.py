import numpy as np;

@profile
def test():
    n = 10000;
    A = np.random.rand(n,n);
    B = np.random.rand(n,n);
    C = A+B;
    print(np.trace(C));
    
    
test();
