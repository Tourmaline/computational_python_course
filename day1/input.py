if __name__ == '__main__':
    import sys;
    mylist = []
    # convert strings from sys.argv to intergers
    for arg in sys.argv[1:]:
        mylist.append(int(arg))
    print(mylist)
