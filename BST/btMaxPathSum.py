# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#wanna start at left leaves and go back and explore
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxP = float("-inf")
        def maxGain(root):
            nonlocal maxP
            if not root:
                return 0
            
            #max between 0 and path of left and right
            #if the value is negative then no reason to consider them
            leftGain = max(maxGain(root.left), 0)
            rightGain = max(maxGain(root.right), 0)
            
            currMaxP = root.val + leftGain + rightGain
            maxP = max(maxP, currMaxP)
            
            return root.val + max(leftGain, rightGain)
        
        maxGain(root)
        return maxP