def sort01(array):
    index = 0
    start = 0
    end = len(array) - 1
    while index <=end:
        if array[index] == 0:
            index +=1
        else:
            array[end],array[index]= array[index],array[end]
            end -=1

A = [1, 0, 1, 0, 1, 1, 0, 1, 0, 0,1]
sort01(A)
print(A)
