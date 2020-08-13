
def rec_power(n, m):
    if m != 0:
        power = n * rec_power(n, m-1)
        return power

    else:
        return 1

print rec_power(58, 4)

