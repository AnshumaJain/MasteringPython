
input_list = input("Enter the list=")

size = len(input_list)
i = 0
max = 0

for i in range(0, size):
    if input_list[i] > max:
        max = input_list[i]

print max


 # [1,2,3], [7, 5, 6, 1]