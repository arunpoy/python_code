import sys  #brute force method O(n^2)
def smallestDifference(array1,array2):
    smallest = sys.maxsize
    smallestPair = []

    for i in range(len(array1)):
        for j in range(len(array2)):
            currentDiff = abs(array1[i] - array2[j])
            if currentDiff < smallest:
                smallest = currentDiff
                smallestPair=[array1[i],array2[j]]
    return[smallestPair]


array1 = [1, 3, 15, 11, 2]
array2 = [23, 127, 235, 19, 8]

print(smallestDifference(array1,array2))
