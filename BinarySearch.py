#Runtime: O(lg n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            #avoid overflow
            mid = left + (right - left) // 2
            if(nums[mid] == target): return mid
            
            #if mid point greater than target, right is set to mid
            if(nums[mid] > target): right = mid - 1
            else: left = mid+1
        
        return -1