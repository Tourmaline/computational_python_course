def f(l):
    print(id(l))
    l = [1,2,3] # to modify l which is outside of the function we can use l[:] = [1,2,3], but it is not recommended due to potential problems because of  function's side effects 
    print(id(l))
    print("inside function ", l)
    val = 4
    return l, val


if __name__ == '__main__':
    i = [5,6]
    print(id(i))
    (l, val) = f(i)
    print(id(i))
    print(l)
    
    print(i)