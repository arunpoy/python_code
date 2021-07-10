import heapq
def kthSmallest(arr, k):
    smallest = []
    for value in arr:
        if (len(smallest) < k):
            heapq.heappush(smallest, -value)
        else:
            heapq.heappushpop(smallest, -value)
    if (len(smallest) < k):
        return None
    return -smallest[0]

def kthmax(k, list):
    if (k == 1):
        return max(list)
    else:
        m = max(list)
        return(kthmax(k-1, [x for x in list if x != m]))


print(kthmax(1,[4, 6, 2, 7, 3, 2, 6, 6]))
print (kthSmallest([2,4,5,7,1],3))
