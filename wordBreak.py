class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        #Keep track of whether a word in the dict ends at this index
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(1,n+1):
            for w in wordDict:
                #If a word ends at current index and the substring matches a word in the dict, set to true
                if dp[i-len(w)] and s[i-len(w):i]==w:
                    dp[i]=True
        return dp[-1]