# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):
        output = []
        self.inOrder(root, output)
        
        for i in range(1, len(output)):
            #with inOrder array should be in increasing order
            if output[i-1] >= output[i]:
                return False

        return True
    
    #Traverse and build an array of BST inOrder
    def inOrder(self, root, output):
        if root is None:
            return
        
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)
        
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     def checkBST(curr, left, right):
    #         if not curr: return True
    #         if not left < curr.val < right:
    #             return False
            ##Go left and check curr.val > left, go right and check curr.val < right
    #         return checkBST(curr.left, left, curr.val) and checkBST(curr.right, curr.val, right)
    #     return checkBST(root, float("-inf"), float("inf"))
    