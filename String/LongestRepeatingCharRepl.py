#Runtime: O(N)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount = 0
        start = 0
        res = 0
        charCount = {}
        #Go through each character in 's'
        for end in range(len(s)):
            #Add each character in 's' to dict 'charCount'
            charCount[s[end]] = charCount.get(s[end], 0) + 1
            
            #maxCount should be the largest character count found so far
            maxCount = max(maxCount, charCount[s[end]])
           
            #if the max char freq and dist in window is greater than k
            #have to shrink window by increasing start
            if(end - start - maxCount + 1 > k):
                charCount[s[start]]-=1
                start+=1
            
            res = max(res, end - start + 1)
        
        return res