x= [3,4,5]

def fun(a):
    a.append(6)
    print(a)

fun(x)
print(x)

def fun1(b):
    b[1]=6
    b[2]=7
    b[3]=8
    print(b)

fun1(x)
print(x)
