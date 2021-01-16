def sortedOrNot(lst):
    idx = 1
    while idx < len(lst):
        if lst[idx]  < lst[idx-1]:

            return False
        
        idx = idx + 1
    return True


lst = [1,2,5,8,4]

if(sortedOrNot(lst)):
    print("sorted")
else:
    print("not sorted")
