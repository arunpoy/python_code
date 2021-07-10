def reverse_string(str):
    rev=""
    for i in str:
        rev=i+rev
    return rev

print(reverse_string("arun"))



def reverseString(str):
    start = 0
    end = len(str) - 1
    while start < end:
        str[start],str[end]= str[end],str[start]
        start +=1
        end -=1
    print(str)

reverseString(["h","e","l","1","o"])

def palindromeCheck(str):
    start = 0
    end = len(str) - 1
    while start < end:
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1
    else:
        return True

print(palindromeCheck("malayala"))
