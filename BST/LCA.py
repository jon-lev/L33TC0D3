# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#LCA will have to be a value that is inbetween the values of p and q (or equal to one of them)
#Set curr to left if curr is greater than the max of p,q (curr too big)
#Set curr to right if curr is less than min of p,q (curr too small)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while(root):
            curr = root.val
            if(curr > max(p.val,q.val)):
                root = root.left
            elif(curr < min(p.val,q.val)):
                root = root.right
            else:
                return root