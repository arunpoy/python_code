def reverseArray(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start],array[end] = array[end],array[start]
        start += 1
        end -= 1

array = [1,2,3,4,5]
print(array)
reverseArray(array)
print(array)

for idx in reversed(range(len(array))):
    print(idx)