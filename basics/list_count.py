def list_count4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count+1
    return count

print(list_count4([1,4,5,6,74,4]))
