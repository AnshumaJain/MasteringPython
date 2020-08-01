
input_string = input("Enter the string = ")
size = len(input_string)
a = size-1

for i in range(0, a):
    if input_string[i] == input_string[a-i] and i != (a-i - 1) and i != (a-i):
        pass
    elif input_string[i] == input_string[a-i]:
        print "it's a palindrome"
        break
    else:
        print "it's not a palindrome"
        break


