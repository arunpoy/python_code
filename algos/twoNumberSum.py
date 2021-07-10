def twoNumberSum(array,targetSum):
    numbers = {}
    for i in array:
        num = targetSum - i
        if num in numbers:
            return[num,i]
        else:
            numbers[i]= True
    return[]

print(twoNumberSum([1,3,5],9))
