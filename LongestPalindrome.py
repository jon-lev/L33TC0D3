class Solution:
    def longestPalindrome(self, s: str) -> int:
        #Can use all letters besides the ones that appear an odd number of times (can only use an odd once)
        
        #Array to store all 128 possible ASCII
        count = [0]*128
        
        #Count all occurences of chars
        for c in s:
            count[ord(c)]+=1
        
        #Count all occurences of odd numbers 
        oddCount = 0
        for c in count:
            oddCount += c & 1
      
        #Longest palindrome is len of string minus the number of odd letters
        return len(s) - oddCount + (oddCount > 0)
        
        