def binarySearch(array,target):
    low = 0
    high = len(array) - 1
    while low <= high:
        middle = (low + high) // 2
        potentialMatch = array[middle]
        if potentialMatch == target:
            return middle
        elif target < potentialMatch:
            high = middle -1
        else:
            low = middle+1

    return -1





array = [10,20,30,40,50]
target = 20
print(binarySearch(array,target))