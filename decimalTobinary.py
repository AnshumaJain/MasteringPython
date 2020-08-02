"""
Given an integer num, convert it into a 32-bit binary
number using a list representation
"""


def decimal_to_binary(num):
    binary = []
    while num >= 1:
        r = (num % 2)
        binary.append(r)
        num = (num // 2)
    binary.reverse()

    p = 32 - len(binary)
    zeros = p * [0]  # create a list of zeros with length p
    zeros.extend(binary)  # append binary list to zeros list

    return zeros

if __name__ == "__main__":
    print(decimal_to_binary(101))