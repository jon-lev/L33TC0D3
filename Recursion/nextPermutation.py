#Algorithm steps: https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/next-permutation-algorithm.svg
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1  
        while nums[right-1] >= nums[right] and right > 0:
            right -= 1
        if right == 0:
            return self.reverse(nums,0,len(nums)-1)
        
        pivot = right - 1
        successor = 0
        
        #find farthest right successor to pivot
        for i in range(len(nums)-1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break
        
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        
        #pivot + 1 b/c already swapped with successor
        self.reverse(nums, pivot + 1, len(nums) - 1)
        
        
    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    