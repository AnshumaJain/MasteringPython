
input_list = input("Enter the list =")

size = len(input_list)
i = 0
max = 0
temp = 0
Sec_max = 0

for i in range(0, size):

    if input_list[i] >= max:
        temp = max
        max = input_list[i]
    else:
        if input_list[i] > Sec_max:
            Sec_max = input_list[i]

    if temp > Sec_max and temp != max:
        Sec_max = temp

print "First max no. is " + str(max)
print "Second max no. is " + str(Sec_max)

# [15,2,5,6,3]-
# [1,2,5,6,3]-
# [1,2,3,4,100,5,200]-
# [10,5,20]-
# [10,20,10,20]-
# [1,2,1,2]-
# [10,10,1,1]-