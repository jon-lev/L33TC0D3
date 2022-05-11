#Runtime = O(N^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sort list for ease of finding sums
        nums.sort()
        output = []
        
        #Loop through nums list up to -2 end
        for i in range(len(nums) - 2):
            
            #If the current element != next element
            if i==0 or (i > 0 and nums[i] != nums[i-1]):
                #move lo and hi pointers
                lo = i + 1;
                hi = len(nums) - 1
                
                #want to find the two numbers that will add up to total
                total = 0 - nums[i]
                while(lo < hi):
                    #if elements at lo/hi == total then we found a match
                    if(nums[lo] + nums[hi] == total):
                        #add to output
                        output.append([nums[i],nums[lo], nums[hi]])
                       
                        #skip duplicates
                        while(lo < hi and nums[lo] == nums[lo+1]): lo = lo + 1
                        while(hi > lo and nums[hi] == nums[hi-1]): hi = hi - 1
                        
                        #move both pointers once found match
                        lo = lo + 1
                        hi = hi - 1
                    
                    #no match, if sum of lo and hi are greater than total, bring down hi
                    elif(nums[lo] + nums[hi] > total):
                        hi = hi - 1
                    #otherwise, increase lo
                    else:
                        lo = lo + 1
        return output
