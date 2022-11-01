# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def LCA(root, p, q):
            if not root: return None

             #looking for 'root' can return root
            if root == p or root == q:
                return root

            left = LCA(root.left, p, q)
            right = LCA(root.right, p,q)
            
            #if both left and right are not None, return root of which called
            if left and right:
                return root
            #both p,q in left subtree -- can return first of p and q found for LCA
            if left and not right:
                return left
            #p,q in right subtree -- return first p and q found
            if right and not left:
                return right

        ret = LCA(root,p,q)
        return ret
        