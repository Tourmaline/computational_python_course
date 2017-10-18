import numpy, time

n=2
for j in range(n):
     a=numpy.ones((n,n))
     b=numpy.ones((n,n))
     c=numpy.zeros((n,n))
     t1=time.clock()
     for i in range(n):
        for k in range(n):
            for j in range(n):
                c[i,j]+=a[i,k]*b[k,j]
     #c=numpy.dot(a,b)
     t2=time.clock()
     
     
     
def change_value(X):
    X[2,3] = 4;
    return X

X = numpy.zeros((5,5))
print(X)
change_value(X) # send and return by reference 
print(X)












