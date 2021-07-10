def reverseArray(array):
    low = 0
    high = len(array) - 1
    while low < high:
        array[low],array[high]=array[high],array[low]
        low+=1
        high-=1

array=[1,2,3,4,5]
reverseArray(array)

print(array)