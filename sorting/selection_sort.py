
# input_list = input("Enter the list = ")

def selection_sort(input_list):
    for j in range(0, len(input_list)):
        [min, min_index] = [input_list[j], j]
        for i in range(j, len(input_list)):
            if input_list[i] < min:
                min = input_list[i]
                min_index = i

        temp = input_list[j]
        input_list[j] = min
        input_list[min_index] = temp

    return input_list

# print input_list

#
#
#

test_array = [
              [10,5,20],
              [15,2,5,6,3],
              [1,2,5,6,6,3],
              [1,2,3,4,100,5,200],
              [10,20,10,20],
              [1,2,1,2],
              [10,10,1,1]
            ]

for k in test_array:

    op = selection_sort(k)
    print op