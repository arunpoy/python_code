def checkPalindrome(str):
    low = 0
    high = len(str) - 1

    while (low < high):
        if str[low] != str[high]:
            print("not a palindrome")
            break
        low = low + 1
        high = high = 1
    else:
        print("it is a palindrome")


checkPalindrome("a")
