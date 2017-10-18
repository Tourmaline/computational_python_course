def f(l):
    print(id(l))
    l += [1,2,3] 
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