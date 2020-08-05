"""
Compute the final amount after compound interest given
P = principal amount
i = annual interest rate
t = number of years invested
"""

def CI(principle, rate, time):
    ci = principle * pow(1 + (rate/100), time)
    return str(ci)


if __name__ == "__main__":

    P = float(input("Enter the principle amount: "))
    R = float(input("Enter the annual rate of interest: "))
    t = float(input("Enter the number of years invested: "))

    print("Compound Interest: ", CI(P, R, t))






