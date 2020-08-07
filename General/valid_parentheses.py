"""
LeetCode Problem #20: Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""


def is_valid(s: str) -> bool:

    if len(s) == 0 or len(s) % 2 != 0 or \
            s[0] in [')', ']', '}'] or \
            s[len(s)-1] in ['(', '[', '{']:
        return False
    else:
        count = 0
        temp = []
        for i in s:
            count += 1
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

        if not temp:
            return True
        else:
            return False


if __name__ == "__main__":
    print(is_valid("()"))
    print(is_valid("()[]{}"))
    print(is_valid("(]"))
    print(is_valid("([)]"))
    print(is_valid("{[]}"))

