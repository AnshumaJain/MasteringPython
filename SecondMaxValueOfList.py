# Find the maximum and second maximum value given a list

def find_second_max_in_list(input_list):

    size = len(input_list)
    temp = 0
    temp_prev = 0
    max_val = input_list[0]
    max_prev = 0
    sec_max_val = input_list[0]

    for i in range(0, size):

        if input_list[i] > max_val:
            max_prev = max_val
            max_val = input_list[i]
        else:
            temp_prev = temp
            temp = input_list[i]

        if temp > temp_prev and sec_max_val <= temp:
            sec_max_val = temp
        elif temp_prev > max_prev and sec_max_val <= temp_prev:
            sec_max_val = temp_prev
        elif sec_max_val <= max_prev:
            sec_max_val = max_prev

    return max_val, sec_max_val


if __name__ == "__main__":

    # [1,2,5,6,3]
    # [1,2,3,4,100,5,200]
    # [10,5,20]
    # [10,20,10,20]
    # [1,2,1,2]
    # [10,10,1,1]
    input_list = eval(input("Enter the list: "))

    max_val, sec_max_val = find_second_max_in_list(input_list)
    print("Second Max: ", str(sec_max_val))
    print("Max: ", str(max_val))
