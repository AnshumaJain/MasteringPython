def plusOne(digits):
    i = len(digits) - 1
    while 1:
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            if i != 0:
                i -= 1
            else:
                return ([1] + digits)

print(plusOne([9,9,9,9]))