# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        def traverse(llist):
            temp = llist
            next_n = 0
            n = ""
            while temp != None:
                next_n = temp.next
                n += str(temp.val)
                temp = next_n
            return int(n[::-1])

        def insert(llist, node):
            return ListNode(node, llist)

        n1 = traverse(l1)
        n2 = traverse(l2)
        n3 = str(n1 + n2)
        ans = ListNode(n3[0])
        
        for digit in n3[1:]:
            ans = insert(ans, int(digit))

        return ans
