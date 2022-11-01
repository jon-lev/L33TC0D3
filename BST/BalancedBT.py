# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ret = True
        
        def dfs(node):
            if not node or not self.ret:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            #difference of subtrees should  be within 1 for them to be balanced
            if abs(left - right) > 1: self.ret = False
            return max(left,right) + 1
        
        dfs(root)
        return self.ret