# Find the maximum value given a list

def find_max_in_list(input_list):

    max_val = input_list[0]
    size = len(input_list)

    for i in range(0, size):
        if input_list[i] > max_val:
            max_val = input_list[i]

    return max_val


if __name__ == "__main__":

    # [1,2,3], [7, 5, 6, 1]
    input_list = eval(input("Enter the list="))

    print(find_max_in_list(input_list))
