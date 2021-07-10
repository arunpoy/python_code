def sort02(array):
    index = 0
    start = 0
    end = len(array) - 1
    while index <=end:
        if array[index] < 0:
            index +=1
        else:
            array[end],array[index]= array[index],array[end]
            end -=1

A = [9, -3, 5, -2, -8, -6, 1, 3]
print(A)
sort02(A)
print(A)