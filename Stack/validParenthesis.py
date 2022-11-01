class Solution:
    def isValid(self, s: str) -> bool:
        #if odd length string, cant be valid
        if len(s) % 2 == 1:
            return False
        
        dic = {'{':'}','(':')','[':']' }
        stack = []
        
        for char in s:
            if char in dic:
                #if the char is [,{,( add to stack to check for closing
                stack.append(char)
            #a closing char then
            #if the stack is empty or doesn't match then it is false
            elif len(stack) == 0 or dic[stack.pop()] != char:
                return False
        return len(stack) == 0
                            