# Swap the first and last elements of the given input list

def swap_first_and_last(input_list):
    i = 0
    n = len(input_list)

    temp = input_list[i]
    input_list[i] = input_list[n-1]
    input_list[n-1] = temp


if __name__ == "__main__":

    # [3,2,4,1,3,6,8]
    input_list = eval(input("Enter the list to be swapped ="))
    swap_first_and_last(input_list)
    print(input_list)

# learn from this:---->
# def swapList(newList):
#     newList[0], newList[-1] = newList[-1], newList[0]
#
#     return newList

# some innovative ideas
# https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/