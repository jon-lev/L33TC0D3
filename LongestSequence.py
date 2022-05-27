#Runtime O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Creating set of numbers takes O(N)
        setNum = set(nums)
        best = 0;
        #Loop through set of nums
        for x in setNum:
            #If the previous number is not in the set (don't want double counting)
            if not x-1 in setNum:
                #Check for next number in sequence
                nextNum = x+1
                while nextNum in setNum:
                    nextNum += 1
                best = max(best, nextNum - x)
        return best