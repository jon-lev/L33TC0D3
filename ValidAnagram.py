#Runtime: O(N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        
        
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        
        for ch in t:
            #If there is a letter that has no count -> hasn't been seen in previous string
            if d.get(ch, 0) == 0: return False
            d[ch] -= 1
            #After decrement, if it is zero then remove it from the dict
            if d[ch] == 0: del d[ch]
            
        #Dict should be empty at end if strings are anagrams
        return len(d) == 0