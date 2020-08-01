
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
# print (decimalToBinary(10))

def calculateHammingDistance(x, y):

    x = decimalToBinary(x)
    print (x)
    y = decimalToBinary(y)
    print (y)

    hamming_dist = 0
    for i in range(0, len(x)):
        if x[i] == y[i]:
            pass
        else:
            hamming_dist += 1

    return hamming_dist


print (calculateHammingDistance(0, 4294967295))

# 0 ≤ x, y < 231