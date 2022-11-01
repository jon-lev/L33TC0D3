class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, degree, ans = defaultdict(list), [0] * numCourses, []
        for nxt,pre in prerequisites:
            graph[pre].append(nxt)
            # +1 to degree for courses that have more prereqs
            degree[nxt]+=1
        
        def dfs(cur):
            #append current course to ans
            ans.append(cur)
            
            #set to -1 to not be visited
            degree[cur] = -1
            
            #for the courses that are connected to the prereq
            for nxtCourse in graph[cur]:
                #subtract the degree (prereq satisifed)
                degree[nxtCourse] -= 1
                
                #if there are no other prereqs for this course
                if degree[nxtCourse] == 0:
                    #run DFS and add it to ans (beginning of DFS)
                    dfs(nxtCourse)
                    
        for i in range(numCourses):
            #if the degree == 0 then theres no prereqs that haven't been visited
            if degree[i] == 0:
                dfs(i)
        
        #answer should be same as num of courses, otherwise a cycle exists
        return ans if len(ans) == numCourses else []