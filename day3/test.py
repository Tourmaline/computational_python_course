# file operations
f = open('t.dat', mode='w');
f.write('hello')
f.close()

# the same with "with" notation:
with open('t.dat', mode='w') as f:
    f.write('hello there')
    # do not need write close
    
    


# import os, subprocess
# subprocess.call("ls -la")

l="Final energy: 3.0".split(':')
print(l)
str_i = l[1]
print(str_i)
i = float(str_i)
print(i)




