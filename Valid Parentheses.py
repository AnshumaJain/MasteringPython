
def isValid(s: str) -> bool:

    if len(s) == 0 or len(s) % 2 != 0 or s[0] in [')',']','}'] or s[len(s)-1] in ['(','[','{']:
        return False
    else:
        count = 0
        temp = []
        for i in s:
            count +=1
            temp.append(i)
            if i == ')':
                if temp[count-2] == '(':
                    temp.pop()
                    temp.pop()
                    count -= 2

            if i == ']':
                if temp[count - 2] == '[':
                    temp.pop()
                    temp.pop()
                    count -= 2

            if i == '}':
                if temp[count - 2] == '{':
                    temp.pop()
                    temp.pop()
                    count -= 2

        if temp == []:
            return True
        else:
            return False








print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))