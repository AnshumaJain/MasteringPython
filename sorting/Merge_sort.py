


def merge_sort(input_list):


    n = len(input_list)
    if n == 1:
        return input_list

    elif n == 0:
        return input_list

    l1 = input_list[0: n/2]
    l2 = input_list[n/2: n]
    andu = merge_sort(l1)
    pandu = merge_sort(l2)

    sorted_merge = []

    i = 0
    j = 0
    while 1:
        if andu[i] <= pandu[j]:
             sorted_merge.append(andu[i])
             i+=1
             if i == len(andu):
                for k in range(j, len(pandu)):
                    sorted_merge.append(pandu[k])
                break
        else:
            sorted_merge.append(pandu[j])
            j+=1
            if j == len(pandu):
                for k in range(i, len(andu)):
                    sorted_merge.append(andu[k])
                break

    return sorted_merge



test_array = [
    [15, 2, 5, 6, 3],
    [1, 2, 5, 6, 4, 3],
    [10, 10, 1, 1],
    [10, 5, 20],
    [1, 2, 3, 4, 100, 5, 200],
    [10, 20, 10, 20],
    [1, 2, 1, 2],
]

for l in test_array:
    op = merge_sort(l)
    print op

