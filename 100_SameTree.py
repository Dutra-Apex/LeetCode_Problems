# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def check_vals(p, q):
            if p and q:
                if p.val == q.val:
                    return check_vals(p.left, q.left) and check_vals(p.right, q.right)
                else:
                    return False
            if not p and not q:
                return True
            else:
                return False
                

        return (check_vals(p,q))
