


def hanoi_rec(n, a, b, c): #(source, helper, destination )

    print(a, b, c)
    print (n)

    if n == 2:
        b.append(a[-1]) # step1
        a.remove(a[-1])
        print(a, b, c)

        c.append(a[-1]) # step2
        a.remove(a[-1])
        print(a, b, c)

        c.append(b[-1]) # step3
        b.remove(b[-1])
        print(a, b, c)

    else:

        hanoi_rec(n - 1, a, c, b)
        print(a, b, c)

        c.append(a[-1])
        a.remove(a[-1])

        hanoi_rec(n - 1, b, a, c)
        print(a, b, c)

    return (a, b, c)



print (hanoi_rec(15, [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [],[]))