
P = float(input("Enter the Principle amount = "))
R = float(input("Enter the Rate of Interest = "))
t = float(input("Enter the Time of deposit = "))

def CI(P, R, t):

    ci = P * (pow((1 + (R/100)), t))
    print "Coumpound_Interest =", str(ci)

CI(P,R,t)






