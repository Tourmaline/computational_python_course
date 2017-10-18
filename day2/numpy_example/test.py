# numpy tests
import numpy

x = numpy.zeros((3,3))
y = x.copy()
print(x is y)


print(numpy.linspace(0, 1, 6))
print(range(5)) # difference between Py2 and Py3
print(list(range(5)))


l1 = [1,2,3]
l2 = [4,5,6]
M = numpy.array([l1,l2])
print(M)


print(M.shape)
MM = M.reshape(6,)
print(MM.shape)
print(MM)

MM[3] = 7
print(M)
print(MM)

for i, v in enumerate(MM):
    print('({}) {}'.format(i, v))
    
    
for i, v in numpy.ndenumerate(M):
    print('{} {}'.format(i, v))
