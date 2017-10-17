d = {7, 88, 7, 9, 101, 99, 4, 3, 3}
print(d)
l = [7, 88, 7, 9, 101, 99, 4, 3, 3]
print(l)
t = (7, 88, 7, 9, 101, 99, 4, 3, 3)
print(t)

print(type(d))
print(type(l))
print(type(t))


# functions

def mymax(x:int,y:int) -> int:
    if x > y:
        return x;
    return y;
    

i = 2;
j = 3;
print("The maximum value of {} and {} is {}".format(i,j,mymax(i,j)))
print(f"The maximum value of {i} and {j} is {mymax(i,j)}")
