"""
LeetCode Problem#38: Count And Say

The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
You can do so recursively, in other words from the previous member read off the digits,
counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.
"""


def count_and_say(n):

    if n == 1:
        return "1"
    elif n == 2:
        return "11"
    else:
        val = count_and_say(n-1)
        prev = 0
        cur = 1
        count = 1
        output = ""
        while 1:
            if val[prev] == val[cur]:
                count += 1
                if cur == (len(val)-1):
                    output += str(count) + str(val[prev])
                    return output
            else:
                output += str(count) + str(val[prev])
                count = 1
                if cur == (len(val) - 1):
                    output += str(count) + str(val[cur])
                    return output
            prev = cur
            cur += 1


if __name__ == "__main__":

    print(count_and_say(5))
    print(count_and_say(10))
