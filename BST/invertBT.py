# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Runtime: O(H)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr:
                #swap left and right, add new pos to stack
                curr.left, curr.right = curr.right, curr.left
                stack.append(curr.left)
                stack.append(curr.right)
        return root