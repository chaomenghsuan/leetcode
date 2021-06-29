import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = []
        for k in range(len(lists)):
            l = lists[k]
            order = 0
            while l:
                q.append((l.val, k, order, l))
                l = l.next
                order += 1
        if not q:
            return None
        heapq.heapify(q)
        head = curr = heapq.heappop(q)[3]
        while q:
            curr.next = heapq.heappop(q)[3]
            curr = curr.next
        return head
            
        
