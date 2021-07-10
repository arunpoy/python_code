def minIndex(array):
    for i in range(len(array)-2):
        for j in range(i+1,len(array)-1):
            if array[j]==array[i]:
                return i

    return -1









array = [2,3,5,4,3,5,2,4]
print(minIndex(array))