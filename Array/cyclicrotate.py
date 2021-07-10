def cyclicRotateArray(array):
    print([array[-1]] + array[0:-1])


array= [1,2,3,4,5]

print(cyclicRotateArray(array))


# def rotate(array):
#     x = array[len(array)-1]
#     for i in range(len(array) - 1, 0, -1):
#         array[i] = array[i - 1];
#     array[0] = x;
#
# rotate(array)
# print(array)