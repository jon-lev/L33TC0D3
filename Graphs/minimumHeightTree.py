class Solution:
    #Idea is to start from all the leaves and start "cutting" the leaves until you reach the center nodes which would have the minimum heights
    #"Any node that has already been a leaf cannot be the root of a MHT, because its adjacent non-leaf node will always be a better candidate."
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #If only one node, return 0
        if n == 1:
            return [0]
        
        #create a graph object to represent edges
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        #leaves will be all nodes with len == 1
        leaves = [node for node in graph if len(graph[node]) == 1 ]
        
        #until node count is smaller/equal to 2
        while n > 2:
            n -= len(leaves)
            nextLeaves = []
            
            #remove leaf nodes
            for leaf in leaves:
                #get the neighbor to the leaf
                neighbor = graph[leaf].pop()
                
                #remove the leaf from the neighbor list of edges
                graph[neighbor].remove(leaf)
                
                #if this makes the neighbor a leaf, add it to leaf lists
                if(len(graph[neighbor]) == 1): nextLeaves.append(neighbor)
            
            #update list of leaves
            leaves = nextLeaves
        return leaves
        