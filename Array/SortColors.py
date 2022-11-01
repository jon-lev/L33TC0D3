#Could trivially do bucketsort (2 passes, one counts, one rewrites)
#Gonna partition array w/ one pass
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0;
        right = len(nums)-1
        i=0;
     
        def swap(i,j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            
        #<= right ensures the array will be sorted            
        while i <= right:
            
            #if we encounter a zero
            if nums[i] == 0:
                #swap with left pointer and increment i and left pointer
                swap(i, left)
                i+=1
                left+=1
            #if encounter a 2
            elif nums[i]==2:
                #swap it with a right, but don't increment i (edge case)
                swap(i, right)
                right-=1
            else:
                i+=1
            