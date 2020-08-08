"""
Given a list and a number N, return a list of the N largest numbers in the list
Example:
    1,3,5,4,6,7
    N = 3
==> [7,6,5]
"""


def list_largest_nums(input_list, N):
    Nmax_list = []

    for j in range(1, N+1):
        ln = len(input_list)
        max_val = 0
        for i in range(0, ln):
            if input_list[i] > max_val:
                max_val = input_list[i]

        Nmax_list.append(max_val)
        if max_val in input_list:
            input_list.remove(max_val)

    return Nmax_list


if __name__ == "__main__":

    # [15,2,5,6,3]
    # [1,2,5,6,6,3]
    # [1,2,3,4,100,5,200]
    # [10,5,20]
    # [10,20,10,20]
    # [1,2,1,2]
    # [10,10,1,1]

    input_list = eval(input("Enter the list="))
    N = int(input("Enter the no. of Max values you want="))

    print(list_largest_nums(input_list, N))
