# Calculate the hamming distance between two integers
from decimal_to_binary import *


def hamming_distance(x, y):

    x = decimal_to_binary(x)
    y = decimal_to_binary(y)

    hamming_dist = 0
    for i in range(0, len(x)):
        if x[i] != y[i]:
            hamming_dist += 1

    return hamming_dist


if __name__ == "__main__":
    # 0 ≤ x, y < 231
    print("A")
    print(hamming_distance(0, 4294967295))
    print("B")
