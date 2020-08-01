
# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.


def sortedSquares(A):
    if len(A) == 0:
        return A
    elif len(A) == 1:
        return [x ** 2 for x in A]

    pos = []
    neg = []
    merge = []
    for i in A:
        if i < 0:
            i *= -1
            neg.append(i)
        else:
            pos.append(i)

    neg = neg[::-1]
    if len(neg) == 0:
        return [x ** 2 for x in pos]
    elif len(pos) == 0:
        return [x ** 2 for x in neg]

    n = 0
    p = 0
    while 1:
        if neg[n] > pos[p]:
            merge.append(pos[p]**2)
            p += 1
            if p == len(pos):
                merge += (x**2 for x in neg[(n):])
                break
        else:
            merge.append(neg[n]**2)
            n += 1
            if n == len(neg):
                merge += (x**2 for x in pos[(p):])
                break
    return merge

print(sortedSquares([-4,-1,0,3,10]))