print("Imported densmatlib.")

import numpy as np;
from numpy import linalg as la;

def msquare(X) :
    #Xsq = la.matrix_power(X, 2);
    # or
    Xsq = X**2;
    return Xsq;

def mtrace(X):
    return np.trace(X);

def mnorm(A,B):
    C = A-B;
    return la.norm(C);


def rand_symm_matrix(n):
    A = np.random.rand(n,n);
    M = np.tril(A) + np.tril(A, -1).T;
    return M;


def choose_branch(method, *arg):
    if method == 'trace_test':
        X=arg[0];
        Xsq = arg[1];
        return True;
    return False;
