# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ret = []
        def dfs(curr, total, path):
            if not curr:
                return
            path.append(curr.val)
            
            #at leaf
            if not curr.left and not curr.right:
                if curr.val + total == targetSum:
                    self.ret.append(path[:])
            else:
                dfs(curr.left, curr.val + total, path)
                dfs(curr.right, curr.val + total, path)
            
            path.pop()
            
        dfs(root, 0, [])
        return self.ret