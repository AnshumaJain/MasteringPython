
def Insertion_Sort(input_list):
    for i in range(0, len(input_list) - 1):
        if input_list[i+1] < input_list[i]:
            temp = input_list[i]
            input_list[i] = input_list[i+1]
            input_list[i + 1] = temp

            my_indices = range(0, i)
            my_indices.reverse()
            for j in my_indices:
                if input_list[j+1] < input_list[j]:
                    temp = input_list[j]
                    input_list[j] = input_list[j+1]
                    input_list[j+1] = temp

    return input_list

test_array = [
              [10,10,1,1],
              [15,2,5,6,3],
              [10,5,20],
              [1,2,5,6,6,3],
              [1,2,3,4,100,5,200],
              [10,20,10,20],
              [1,2,1,2],
            ]

for k in test_array:

    op = Insertion_Sort(k)
    print op