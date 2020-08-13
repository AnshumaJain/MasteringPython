
import copy

class abc():
    def __init__(self):
        # self.m = 1
        self.n = [1, 2, 3]
    #     self.m = 5
    #     self.n = [1,2,3]
    #     self.tin = copy.deepcopy(self.m)
    #     self.tan = copy.deepcopy(self.n)



# create new object
pee = abc()
# poo = copy.deepcopy(pee)

# poo.b = 7
# poo.tin += 5
# poo.tan.append(4)

# print(poo.b)
# print(pee.b)
# print(pee.m)
# print(pee.n)
# print(pee.tin)
# print(pee.tan)


# regular copy
# poo = pee
# poo.m = 50
# poo.n.append(4)
# print(pee.m)
# print(pee.n)

# shallow copy
paa = copy.copy(pee)
paa.m = 500
paa.n[0] = 10
print(pee.m)
print(pee.n)

# deep copy
# gaga = copy.deepcopy(pee)
# gaga.m = 5000
# gaga.n.append(6)
# print(pee.m)
# print(pee.n)