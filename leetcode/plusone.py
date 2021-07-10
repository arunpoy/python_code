# def plusOne(digits):
#     digits = digits[::-1]
#     carry = 1
#     index = 0
#     while carry:
#         if index < len(digits):
#             if digits[index] !=9:
#                 digits[index] +=1
#                 carry = 0
#             else:
#                 digits[index]=0
#         else:
#             digits.append(1)
#             carry = 0
#         index +=1
#     return digits

def plusOne(digits):
    ctr = len(digits) - 1
    carry = 1

    while carry:
        if ctr >= 0:
            if digits[ctr] != 9:
                digits[ctr]+=1
                #carry = 0
                return digits
            else:
                digits[ctr] = 0
                print(digits)
        # else:
        #     digits.append(1)
        #     carry = 0
        #     return digits[::-1]
        ctr -=1
    return digits



digits = [1,9,9]
print(plusOne(digits))
