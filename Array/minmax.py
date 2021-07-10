def minArray(array):
    low = array[0]
    for idx in range(1,len(array)):
        low = min(low,array[idx])
    return low

def maxArray(array):
    high = array[0]
    for idx in range(1,len(array)):
        high = max(high,array[idx])
    return high

array = [100,20,3,40,50]

print(minArray(array))
print(maxArray(array))