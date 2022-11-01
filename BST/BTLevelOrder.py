# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#O(N) = O(V+E)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [root]
        ret = []
        if not root: return []
        while q:
            currNode = []
            nxtLvl = []
            for node in q:
                #create separate array to add to ret after iterating
                currNode.append(node.val)
                #add left to check if it exists
                if node.left:
                    nxtLvl.append(node.left)
                #add right to nxtLvl if it exists
                if node.right:
                    nxtLvl.append(node.right)
            #appending array will have [[]] in ret
            ret.append(currNode)
            q = nxtLvl
                
        return ret