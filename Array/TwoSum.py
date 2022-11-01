#O(N) runtime
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Create an empty dictionary
        dict = {}
        
        #Loop through list
        for i in range(len(nums)):
            #Find difference between element and desired value
            diff = target - nums[i]
            
            #If this desired value is in the dictionary, means we have seen that value before
            if(diff in dict):
                #Return indicies of where diff is in dict and current index 'i'
                return [dict[diff], i]
            else:
                #Otherwise, place the value of element with its index
                dict[nums[i]] = i