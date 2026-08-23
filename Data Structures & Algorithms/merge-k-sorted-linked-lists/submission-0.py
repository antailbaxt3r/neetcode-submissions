# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class Node:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val

        
        if len(lists) == 0:
            return None

        root = ListNode(0)
        curr = root
        minheap = []
        for l in lists:
            if l is not None:
                heapq.heappush(minheap, Node(l))
        while minheap:
            node = heapq.heappop(minheap)
            curr.next = node.node
            curr = curr.next

            if node.node.next:
                heapq.heappush(minheap, Node(node.node.next))
        return root.next