def getSecMax(lst):
    if len(lst)<=1:
        return("there is no second largest")
    lar = lst[0]
    slar = None

    for l in lst[1:]:
        if l > lar:
            slar = lar
            lar = l
        elif l!=lar:
            if slar==None or slar < l:
                slar = l
    return slar

print(getSecMax([20,20,15]))
