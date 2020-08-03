# Find out if the given input string is a palindrome

def is_palindrome(input_string):

    size = len(input_string)
    ln = size - 1
    for i in range(0, ln):
        if input_string[i] == input_string[ln-i] and i != (ln-i - 1) and i != (ln-i):
            pass
        elif input_string[i] == input_string[ln-i]:
            print("it's a palindrome")
            break
        else:
            print("it's not a palindrome")
            break


if __name__ == "__main__":
    input_string = input("Enter the string = ")
    is_palindrome(input_string)
