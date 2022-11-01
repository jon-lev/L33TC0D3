#Runtime: O(N)
#2 Pointer Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        #s = ''.join(e for e in s if e.isalnum()).lower()
        
        while left < right:
            #isalnum() method returns True if all characters in the string are alphanumeric
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left+=1
                    right-=1
        return True
            