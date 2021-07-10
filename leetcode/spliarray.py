def splitArray(array):
    leftSum = 0
    for i in range(len(array)):
        leftSum += array[i]
    print(leftSum)

    rightSum = 0
    for j in range(len(array)):
        rightSum += array[j]

        leftSum -= array[j]
        if leftSum == rightSum:
            return j

    return -1



array = [4, 3, 2, -1]
print(splitArray(array))

