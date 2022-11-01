# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        q = collections.deque()
        if not root: return []
        if root: q.append(root)
        while q:
            #append farthest right .val into return
            ret.append(q[-1].val)
            #for DFS in trees, put for loop inside while to iterate all nodes on queue
            for _ in range(len(q)):
                curr = q.popleft()
                if(curr.left):
                    q.append(curr.left)
                if(curr.right):
                    q.append(curr.right)
                    
        return ret