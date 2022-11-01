#graph problem
#pairs represent edges, arrows represent coursed needed for that course
#if there is a CYCLE then it's impossible
#DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #empty list for every course (adj list to map graph)
        mapping = {i:[] for i in range(numCourses)}
        
        #add to adj list
        for crs, pre in prerequisites:
            mapping[crs].append(pre)
            
        #see if course been visited (if visited 2x, a cycle exists)
        visited = set()
        
        def dfs(crs):
            #if crs already visited, a cycle
            if crs in visited:
                return False
            #if no other pre-reqs left return true and go to next recursion
            if mapping[crs] == []:
                return True
            
            #add crs to visited set
            visited.add(crs)
            
           
            for pre in mapping[crs]:
                #if one course cant get it's prereqs
                if not dfs(pre): return False
            
            #remove from set b/c no longer visiting it
            visited.remove(crs)
            
            #set to empty list to return True if iterates again
            mapping[crs] = []
            
            #course can be taken
            return True
        
        #have to iterate through all courses in case of disconnected graph
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        
#O(numCourses) / O(V+E)