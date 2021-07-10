def firstDuplicate(array):
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1


array = [2,1,3,3,2,5]

print(firstDuplicate(array))