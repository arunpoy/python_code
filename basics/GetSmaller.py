def getSmaller(lst,n):
    res = []
    for l in lst:
        if l < n:
            res.append(l)
    return(res)

print(getSmaller([20,3,4,56,78],10))


# Using List comprehension

def getSmallerUsingComprehension(lst,n):
    return[l for l in lst if l <n]

print(getSmallerUsingComprehension([20,3,4,56,78],10))
