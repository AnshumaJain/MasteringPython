
input_list = input("Enter the list to be swapped =")
i = 0
n = len(input_list)

temp = input_list[i]
input_list[i] = input_list[n-1]
input_list[n-1] = temp

print input_list


# learn from this:---->
# def swapList(newList):
#     newList[0], newList[-1] = newList[-1], newList[0]
#
#     return newList

# some innovative ideas
# https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/