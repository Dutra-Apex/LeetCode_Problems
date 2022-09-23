# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
    
        if head.next == None:
            return head
           
        temp = head.next
        prev = head
        
        while temp != None:
            if temp.val == prev.val:   
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next


        return head
