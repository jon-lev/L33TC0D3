# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #storing the node, and position on bt
        q = [(root,0)]
        ans = 0
        
        while q:
            #ans will equal last value position from first value position in same level
            ans = max(ans, q[-1][1] - q[0][1] + 1)
            t = []
            for node, i in q:
                # 2* i determines its position "number" to do calculation on
                if node.left: t.append((node.left, 2 * i))
                if node.right: t.append((node.right, 2 * i + 1))
            
            q = t
            
        return ans