"""
LeetCode Problem #2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        num1 = 0
        i = 0
        temp = l1
        while temp:
            num1 += temp.val * 10 ** i
            i += 1
            temp = temp.next

        num2 = 0
        i = 0
        temp = l2
        while temp:
            num2 += temp.val * 10 ** i
            i += 1
            temp = temp.next

        add = num1 + num2

        count = 0
        temp = add
        while 1:
            temp = temp // 10 ** 1
            count += 1
            if temp == 0:
                break

        l3 = None
        temp = add
        while count != 0:
            digit = temp // (10 ** (count - 1))
            temp = temp % (10 ** (count - 1))
            count -= 1
            l3 = ListNode(digit, l3)

        return l3


if __name__ == "__main__":

    sol = Solution()

    list_node1 = ListNode(2, ListNode(4, ListNode(3, None)))
    list_node2 = ListNode(5, ListNode(6, ListNode(4, None)))

    list_node3 = sol.add_two_numbers(list_node1, list_node2)
    print(list_node3.val)
    print(list_node3.next.val)
    print(list_node3.next.next.val)