array = [1,2,2,3,4,5,5,6]


def findDuplicates(array):
    start = 0
    result=[]
    for i in range(1,len(array)):
        if array[i] != array[start]:
            start = start + 1
        elif if array[i] == array[start]:
            result.append(array[start])
            
