class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #If is empty
        if not strs:
            return ""
        
        #Find smallest string in list
        shortest = min(strs, key=len)
        
        #For every char and index in the shortest string
        for i, ch in enumerate(shortest):
            #for the other strings in strs list
            for other in strs:
                #if their character at index 1 != ch
                if other[i] != ch:
                    #Return up to index
                    return shortest[:i]
        return shortest