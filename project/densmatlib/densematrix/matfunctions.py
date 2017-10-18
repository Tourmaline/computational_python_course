import numpy as np;
from numpy import linalg as la;

def msquare(X) :
    Xsq = X**2;
    return Xsq;

def mtrace(X):
    return np.trace(X);

def mnorm2_diff(A,B):
    C = A-B;
    return la.norm(C);


def rand_symm_matrix(n):
    A = np.random.rand(n,n);
    M = np.tril(A) + np.tril(A, -1).T;
    return M

def diag_matrix(D):
    M=np.diag(D)
    return M
