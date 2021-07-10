def binarySearch(array,target,leftBias):
    l,r = 0, len(array) - 1
    i = -1
    while l <= r:
        mid = (l+r)//2
        if target < array[mid]:
            r = mid - 1
        elif target > array[mid]:
            l = mid + 1
        else:
            i = mid
            if leftBias:
                r = mid -1
            else:
                l = mid+1
    return i

def searchRange(array,target):
    left = binarySearch(array,target,True)
    right= binarySearch(array,target,False)
    return[left,right]

array = [2,2,3,3,4,4,4,5,5]
target = 4
print(searchRange(array,target))
print(binarySearch(array,target,False) - binarySearch(array,target,True) + 1)
