odd = []
even = []
def getOddEven(lst):

    for l in lst:
        if l%2 == 0:
            even.append(l)
        else:
            odd.append(l)
    return(odd,even)

odd,even = print(getOddEven([20,31,42,57]))

print(odd)
print(even)

#using list comprehension
