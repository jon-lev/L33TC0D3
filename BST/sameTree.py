# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #if both at leaves, iterated throughout whole tree
        if not p and not q:
            return True
        #if only one is at leaf, not correct
        if not p or not q:
            return False
        else:
            if p.val == q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
            else:
                return False