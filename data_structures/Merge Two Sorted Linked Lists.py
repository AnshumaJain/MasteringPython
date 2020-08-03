
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

    list1 = l1
    list2 = l2
    sort_list = listnode()
    if l1.val >= l2.val:
