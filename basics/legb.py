#LEGB Local, enclosing, global, builtin
import builtins
x = 'Global x'

def test():
    #global x
    x = 'Local x'
    print(x)

test()
print(x)
print(dir(builtins))
