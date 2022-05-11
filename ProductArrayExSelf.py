#Runtime = O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        p = 1
        output = []
        
        #Calculating products of left->right
        #nums=[1,2,3,4, 5]
        #output = [1, 1, 2, 6, 24]
        for i in range(len(nums)):
            output.append(p)
            p = p * nums[i]
            
        p = 1
        
        #Calculating products from right -> left
        #nums=[1,2,3,4,5]
        #prevOutput = [1, 1, 2, 6, 24]
        #output = [120,60,40,30,24]
        for i in range(len(nums)-1,-1,-1):
            output[i] = output[i] * p
            p = nums[i] * p
            
        return output