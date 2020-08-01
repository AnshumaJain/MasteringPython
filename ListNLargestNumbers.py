input_list = input("Enter the list=")
N = input("Enter the no. of Max values you want=")

Nmax_list = []
max = 0

for j in range(1, (N+1)):
    for i in range(0, len(input_list)):
        if input_list[i] > max:
            max = input_list[i]

    Nmax_list.append(max)
    input_list.remove(max)
    max = 0


print Nmax_list

# [15,2,5,6,3]
# [1,2,5,6,6,3]
# [1,2,3,4,100,5,200]
# [10,5,20]
# [10,20,10,20]
# [1,2,1,2]
# [10,10,1,1]