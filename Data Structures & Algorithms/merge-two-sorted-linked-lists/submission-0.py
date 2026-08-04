# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = ListNode()
        answer = head
        while p1 and p2:
            if p1.val < p2.val:
                head.next = p1
                p1 = p1.next
            else:
                head.next = p2
                p2 = p2.next
            head = head.next
        head.next = p1 or p2
        return answer.next

                