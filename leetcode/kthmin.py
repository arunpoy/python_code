# def findKthMin(array,k):
#     array.sort()
#     return array[k-1]
# array = [2,4,3,5,1]
# k=2
# print(findKthMin(array,k))
# naive approach O(nlogn)
import heapq
from heapq import heappop

def findKthMin(array,k):
    heapq.heapify(array)
    print(array)
    while k > 1:
        heappop(array)
        print(array)
        k = k - 1
    return array[0]


A = [7, 4, 6, 3, 9, 1]
k = 3

print("k'th smallest element in the list is", findKthMin(A,k))