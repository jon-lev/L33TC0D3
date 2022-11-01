# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#1st val in preorder is always root

#find root val in inorder, all values to left of it are in left subtree all values in right are in right subtree

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        #preorder of 1 -> mid (not inclusive +1)
        #inorder up to mid, not including
        #partition for left subtree up to mid
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        #mid + 1 will partition for right subtree
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root