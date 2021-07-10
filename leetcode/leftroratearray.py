def leftRotateArray(array):
    for i in range(2):
        array = [array[-1]] + array[0:-1]
    return array



A = [1, 2, 3, 4, 5]

print(leftRotateArray(A))

