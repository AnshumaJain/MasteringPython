input_list = input("Enter the list =")

size = len(input_list)
i = 0
max_prev = 0
max = 0
temp_prev = 0
temp = 0
Sec_max = 0


for i in range(0, size):

    if input_list[i] > max:
        max_prev = max
        max = input_list[i]
    else:
        temp_prev = temp
        temp = input_list[i]

    if temp > temp_prev and Sec_max <= temp:
        Sec_max = temp
    elif temp_prev > max_prev and Sec_max <= temp_prev:
        Sec_max = temp_prev
    elif Sec_max <= max_prev:
        Sec_max = max_prev


    print max_prev, max, temp_prev, temp, Sec_max


print "secondmax" + str(Sec_max)
print "max" + str(max)
#print "temp" + str(temp)

#  [1,2,5,6,3]
# [1,2,3,4,100,5,200]
# [10,5,20]
# [10,20,10,20]
[1,2,1,2]
[10,10,1,1]