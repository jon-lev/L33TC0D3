#Runtime = O(2^t) (target is height)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, num: List[int], target: int, path: str, ret: List[List[int]]):
        #If passed target, return
        if target < 0:
            return
        #If target == 0, found combination, add to return
        if target == 0:
            ret.append(path)
            return
        #Loop through all values skipping number each time to avoid dupes
        for i in range(len(num)):
            self.dfs(num[i:], target - num[i], path+[num[i]], ret)
        