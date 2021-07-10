lst = [1,2,3,4]

# print(lst)
#
# for i in lst:
#     print(i)
#
# for i in range(len(lst)):
#     print(lst[i])
#
# for i in reversed(range(len(lst))):
#     print(lst[i])

# for i in range(len(lst)-1):
#     print(i)

# squares = []
# for value in lst:
#     square = value**2
#     squares.append(square)
#
# print (squares)

squares = [value **2 for value in lst]
print(squares)