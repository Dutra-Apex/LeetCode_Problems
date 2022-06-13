# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        a = b = ListNode()
        
        while not (list1 is None or list2 is None):
            
            if list1.val < list2.val:    
                current = list1
                list1 = list1.next
            else:
                current = list2
                list2 = list2.next
                
            b.next = current
            b = b.next
            
        b.next = list1 or list2
        
