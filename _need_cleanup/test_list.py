

def swap(a,b):
    temp = b[0]
    b[0] = a[0]
    a[0] = temp

    return a,b

a = [1,2,3]
b = [5,6,7]
swap(a,b)
print(a)
print(b)