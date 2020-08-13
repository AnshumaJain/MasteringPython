# Find out if the given nubler is a power of 2
# (i.e. it can be represented as 2^x where X is an integer)


def two_power(num):
    if num % 2 == 0:
        x = num / 2

        if x == 1:
            print("Yes! This number is a power of 2!")
        else:
            two_power(x)

    else:
        print("No, this number is a *NOT* a power of 2.")


if __name__ == "__main__":
    num = 256
    two_power(num)

