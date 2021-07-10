def findMin(array):
    res = array[0]
    l,r = 0 , len(array) - 1
    while l <=r :
        if array[l]<array[r]:
            res = min(array[l],res)
            break
        m = (l+r)//2
        res = min(res,array[m])
        if array[m] >= array[l]:
            l = m + 1
        else:
            r = m - 1
    return res

array = [3,4,5,2,1]

print(findMin(array))