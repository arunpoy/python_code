def myfun(message,char='-'):
    output = char * len(message)
    print(output)
    print(message)
    print(output)

myfun("hi there",'#')
