def sortNumbers(array):
    start = 0
    end = len(array) - 1
    index = 0
    while index <= end :
        if array[index]==0:
            array[index],array[start] = array[start],array[index]
            start += 1
            index += 1
        elif array[index]==2:
            array[index], array[end] = array[end], array[index]
            end -= 1
        else:
            index += 1

A = [1,1,1,1,2,2,2,0]
sortNumbers(A)
print(A)
