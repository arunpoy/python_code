# def reverseWords(string):
#     lst = string.split(" ")
#     print(lst)
#     for i in range(len(lst)-1,-1,-1):
#         print(lst[i], end = " ")
#
# reverseWords("geeks is best")


def reverseWordsInString(string):
    array = string.split(" ")
    rev = " "
    for idx in range(len(array) - 1, -1, -1):
         #print(array[idx], end =" ")
         rev = rev + array[idx] + " "
         print(rev)

    return rev

print(reverseWordsInString("AlgoExpert is the best!"))