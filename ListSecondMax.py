# Find the maximum and second maximum value given a list

def find_second_max_in_list(input_list):

    size = len(input_list)
    max_val = input_list[0]
    temp = 0
    sec_max_val = input_list[0]

    for i in range(0, size):

        if input_list[i] >= max_val:
            temp = max_val
            max_val = input_list[i]
        else:
            if input_list[i] > sec_max_val:
                sec_max_val = input_list[i]

        if temp > sec_max_val and temp != max_val:
            sec_max_val = temp

    return max_val, sec_max_val


if __name__ == "__main__":

    # [15,2,5,6,3]-
    # [1,2,5,6,3]-
    # [1,2,3,4,100,5,200]-
    # [10,5,20]-
    # [10,20,10,20]-
    # [1,2,1,2]-
    # [10,10,1,1]-
    input_list = eval(input("Enter the list ="))

    max_val, sec_max_val = find_second_max_in_list(input_list)
    print("First max no. is:", str(max_val))
    print("Second max no. is:", str(sec_max_val))
