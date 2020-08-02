

def CI(principle, rate, time):
    ci = principle * pow(1 + (rate/100), time)
    return str(ci)

if __name__ == "__main__":

    P = float(input("Enter the Principle amount: "))
    R = float(input("Enter the Rate of Interest: "))
    t = float(input("Enter the Time of deposit: "))

    print("Compound Interest: ", CI(P, R, t))






