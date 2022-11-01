class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char == "[":
                # finished calculating k, save current string and k for when we pop
                stack.append((current_string, k))
                # Reset current_string and k
                current_string = ""
                k = 0
            elif char == "]":
                #completed frame, get last current_string and k
                # is the k we need to duplicate the current current_string by
                last_string, last_k = stack.pop()
                current_string = last_string + last_k * current_string
            elif char.isdigit():
                #to prevent more than single digit numbers from messing up 
                k = k * 10 + int(char)
            else:
                current_string += char

        return current_string