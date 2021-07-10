def isPalindrome(x):
        num = x
        rev = 0
        rtype = False
        if x < 0:
            return False
        while num > 0:
            n = num%10
            rev = rev*10 + n
            num = num//10
        print(rev)
        print()
        if rev == x or x == 1:
            print(" i am here")
            rtype = True
        return rtype
print (isPalindrome(1))
