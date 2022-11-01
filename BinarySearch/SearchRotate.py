class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            #If target is less than 0 value and less than midpoint
            if target < nums[0] < nums[mid]:
                left = mid + 1
                
            #If target is greater than first element and midpoint
            elif target >= nums[0] > nums[mid]:
                right = mid
                
            #Normal binary search statements
            elif target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1