
def decimalToBinary(num):
    binry = []
    while num >= 1:
        r = (num % 2)
        binry.append(r)
        num = (num // 2)
    binry.reverse()
    p = 32 - len(binry)
    zeros = p * [0]
    zeros.extend(binry)
    return zeros