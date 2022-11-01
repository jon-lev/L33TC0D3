class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dictP = collections.Counter(p)
        #Loading dict with only length of p chars b/c anagram must be p length long
        dictS = collections.Counter(s[:len(p)])
        output = []
        
        i = 0
        j = len(p)
        size = len(s)
        
        #While window size less than length of S
        while j <= size:
            #If count of chars in dictS = chars in dictP, it's an anagram
            if dictP == dictS:
                output.append(i)
            
            #If window length still less than length of S
            if j < size:
                #Add count to char not looked at yet
                dictS[s[j]] += 1
                
            #Remove count for previous char being assessed
            dictS[s[i]] -= 1
            
            #If the count gets to zero, remove it from list
            if dictS[s[i]] == 0:
                del dictS[s[i]]
                            
            i+=1
            j+=1
        return output
        