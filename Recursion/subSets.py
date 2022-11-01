class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        
        for n in nums:
            for i in range(len(ret)):
                ret.append(ret[i] + [n])
        
        return ret