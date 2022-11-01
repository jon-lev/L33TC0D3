class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ##Pretty basic way to do it, majority number will be in the middle
        # nums.sort()
        # return nums[len(nums)//2]
        
        # Boyer's Moore Algorithm --> O(1) Space, O(N)
        #https://www.cs.utexas.edu/~moore/best-ideas/mjrty/
        count = 0
        candidate = nums[0]
        for num in nums:
            if num==candidate:
                count+=1
            elif count == 0:
                candidate = num
                count = 1
            else:
                count-=1
        return candidate
                