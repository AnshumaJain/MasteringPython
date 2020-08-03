# Return the sum of all the values in the given input list

def list_sum(input_list):
        sum = 0
        for i in range(0, len(input_list)):
                sum = sum + input_list[i]

        return sum


if __name__ == "__main__":

        # [1,2,3], [4, 5, 6, 10]
        input_list = eval(input("Enter the list to be added ="))
        print(list_sum(input_list))
