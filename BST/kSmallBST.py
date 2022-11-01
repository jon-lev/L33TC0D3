# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#O(N)
#make sure all self.VAR for recursion to work properly
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node):
            if not node or self.found:
                return
            helper(node.left)
            #subtract one from k for every iteration
            self.k -= 1
            
            #once == 0 found correct spot by going left (less)
            if self.k == 0:
                self.res = node.val
                self.found = True
                return
            helper(node.right)
        
        self.res = None
        self.k = k
        self.found = False
        helper(root)
        return self.res