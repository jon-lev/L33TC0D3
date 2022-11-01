#Runtime O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            #if the curSum became negative, only add curr num
            curSum = max(curSum, 0) + num
            maxSum = max(curSum, maxSum)
        
        return maxSum