#Runtime O(N)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if(len(nums) > 1):
            k = k % len(nums)
            #Reverse entire list
            #[1,2,3,4,5,6,7] k=3
            self.reverse(nums, 0, len(nums)-1)
            #[7,6,5,4,3,2,1] k=3
            
            #Reverse first half of list to k
            self.reverse(nums, 0, k-1)
            #[5,6,7,4,3,2,1] k=3
            
            #Reverse the rest of the list
            self.reverse(nums, k, len(nums)-1)
            #[5,6,7,1,2,3,4] k=3

    def reverse(self, nums, start, end) -> None:
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start+=1
            end-=1