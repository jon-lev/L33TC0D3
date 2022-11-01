class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, used, ret):
            if len(path) == len(nums):
                #need to append [:] so not blank path in function declaration getting added
                ret.append(path[:])
                return
            
            for i, letter in enumerate(nums):
                #if the number used before, skip it
                if used[i]:
                    continue
                    
                #add it to path
                path.append(letter)
                
                #set used to true
                used[i] = True
                dfs(path, used, ret)
                
                
                used[i] = False
                path.pop()
        
        ret = []
        dfs([], [False] * len(nums), ret)
        return ret