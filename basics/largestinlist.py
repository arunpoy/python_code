'''def getLargest(lst):
    if len(lst) == 0:
        return("the list is empty")
    else:
        lar = lst[0]
        for l in range(1,len(lst)):
            if lst[l] > lar:
                lar= lst[l]
        return lar


print(getLargest([1,45,62,33]))

print(getLargest([])) '''

def getLargest(lst):
    if len(lst) == 0:
        return("the list is empty")
    else:
        lar = lst[0]
        for l in lst[1:]:
            if l > lar:
                lar= l
        return lar

print(getLargest([1,45,62,33]))

print(getLargest([]))
