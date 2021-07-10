def searchInsert(array,target):
    l,r = 0, len(array) - 1
    while l <= r:
        mid = (l+r) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            l = mid + 1
        else:
            r = mid -1
    return l


array = [1,3,4,5]

target = 2

print(searchInsert(array,target))