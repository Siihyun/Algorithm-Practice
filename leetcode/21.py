# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#using iteration

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0,None);
        last = head
        while l1 and l2:
            if l1.val < l2.val:
                last.next = l1
                last = last.next
                l1 = l1.next
            else:
                last.next = l2
                last = last.next
                l2 = l2.next
        
        while l1:
            last.next = l1
            last = last.next
            l1 = l1.next
        
        while l2:
            last.next = l2
            last = last.next
            l2 = l2.next
            
        return head.next
            
            

#using recursion
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1,l2 = l2,l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next,l2)
        return l1