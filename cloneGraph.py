"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        
        #Queue to iterate through the neighbors
        queue = deque([node])
        
        #Dict storing the value of the node to a new Node object with it's value contained and empty neighbors (will be building neighbors based off original node)
        clone = {node.val: Node(node.val)}
        
        
        while queue:
            #Get neighbor to check
            curr = queue.popleft()
            
            #Get clone of it to check if neighbors there or not
            currClone = clone[curr.val]
            
            #Loop through the neighbors of current node
            for neigh in curr.neighbors:
                
                #If the neighbor is not in the clone
                if neigh.val not in clone:
                    #Add neigh to the clone
                    clone[neigh.val] = Node(neigh.val)
                    #Append neigh to the queue to check next if all of 'neigh' neighbors are cloned
                    queue.append(neigh)
                
                #Add the cloned node to the current cloned nodes neighbors
                currClone.neighbors.append(clone[neigh.val])
        
        #Return the clone version from first nodes value
        return clone[node.val]
                