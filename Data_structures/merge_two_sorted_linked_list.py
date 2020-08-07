"""
LeetCode Problem #21: Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        p1 = l1
        p2 = l2

        if p1.val <= p2.val:
            head = p1
            prev = p1
            if p1.next is None:
                prev.next = p2
                return head
            p1 = p1.next
        else:
            head = p2
            prev = p2
            if p2.next is None:
                prev.next = p1
                return head
            p2 = p2.next

        while 1:

            if p1.val <= p2.val:
                prev.next = p1
                prev = p1
                if p1.next is None:
                    prev.next = p2
                    break
                p1 = p1.next

            else:
                prev.next = p2
                prev = p2
                if p2.next is None:
                    prev.next = p1
                    break
                p2 = p2.next

            if prev.next is None:
                break

        return head


if __name__ == "__main__":

    sol = Solution()

    list_node1 = ListNode(1, ListNode(2, ListNode(4, None)))
    list_node2 = ListNode(1, ListNode(3, ListNode(4, None)))

    list_node3 = sol.merge_two_lists(list_node1, list_node2)
    print(list_node3.val)
    print(list_node3.next.val)
    print(list_node3.next.next.val)
    print(list_node3.next.next.next.val)
    print(list_node3.next.next.next.next.val)
    print(list_node3.next.next.next.next.next.val)
