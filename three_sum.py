"""
Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array
which gives the sum of zero.
"""


def three_sum(nums):
    my_set = []
    my_dict = {}
    for a in nums:  # for element 'a' in nums
        for index, c in enumerate(nums):  # for element 'c' in nums
            b = - (a + c)  # calculate value of 'b' to make a+b+c=0
            if a != c and b != c and a != b:  # if a,b,c are different
                if b not in my_dict:
                    my_dict[c] = index
                else:
                    list = [a, b, c]
                    my_set.append(list)

    #print("dict:", my_dict)
    return my_set


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
