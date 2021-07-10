def removeDuplicates(array):
    start = 0
    array1 = []
    for i in range(1,len(array)):
        if array[i] != array[start]:
            start = start + 1
            array[start] = array[i]
            print(array)


    return start


array = [1,1,1,2,2,3,3,4]

print(removeDuplicates(array))
