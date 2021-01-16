def arguments(*args, **kwargs):
    print('positional arguments ', args)
    print('keyword arguments ', kwargs)


arguments(1,2,3,four=4,five=5)
