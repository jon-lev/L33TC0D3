class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        start = 0
        for i, ch in enumerate(s):
            # when char in dictionary
            if ch in dic:
                # check length from start of string to index against return
                res = max(res, i-start)
                # update start of string index to the next index b/c had repeating character
                start = max(start, dic[ch]+1)
            # add/update char to/of dictionary 
            dic[ch] = i
        # answer is either res or difference between last start that wasn't calculated
        return max(res, len(s)-start)