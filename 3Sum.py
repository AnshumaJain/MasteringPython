def threeSum(nums):

    set = []
    h = {}
    for i in nums:
        a = i
        for j, c in enumerate(nums):
            b = - (a + c)
            if a != c and b != c and a != b:
                if b not in h:
                    h[c] = j
                else:
                    list = []
                    list.append(a)
                    list.append(b)
                    list.append(c)
                    set.append(list)
    print("dict = ", h)
    print("list = ", list)
    return set

print(threeSum([-1, 0, 1, 2, -1, -4]))

