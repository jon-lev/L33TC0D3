#Runtime: O(N^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            #odd case #aba
            temp = self.findPalindrome(s, i, i)
            if len(temp) > len(res):
                res = temp
            #even case #abba
            temp = self.findPalindrome(s, i, i+1)
            if len(temp) > len(res):
                res = temp
        return res
    
    def findPalindrome(self, s, l, r) -> str:
        #if left pointer not at end and right pointer not at end and pointers chars match, keep moving to find another palindrome
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]