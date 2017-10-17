import numpy as np;
import random

@profile
def test():
    n = 10000;
    A = np.random.rand(n,n);
    #B = A; # reference
    B = A.copy();
    B[1,1] = 1;
    #print(A)
    #print(B)
    C = A+B;
    print(np.trace(C));
    
    m = 100000;
    l = random.sample(range(1, 2*m), m);
    lcopy = l.copy();
    # p = random.sample(range(1, 2*m), m);
    # #print(l)
    # l.append(p);
    # #print(l)
    # p[6] = 5;
    # #print(l)
    # print(len(l))

    l = random.sample(range(1, 2*m), m);
    
    #print(lcopy)
    l = lcopy.copy();
    #l = l+p;
    #print(l)
    
    
    
    
    
test();
