def search(array,target):
    l,r = 0, len(array)-1
    while l <= r:
        mid = (l+r) //2
        if target == array[mid]:
            return mid
        if array[l] <= array[mid]:
            if target > array[mid] or target < array[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < array[mid] or target > array[r]:
                r = mid -1
            else:
                l = mid + 1
    return - 1

array = [4,5,6,7,0,1,2]
target = 0
print(search(array,target))

