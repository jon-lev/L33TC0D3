class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for w in strs:
            #Sort the strings so they would be the same
            key = tuple(sorted(w))
            #If already seen, add unsorted string to corresponding key
            if key in dic:
                dic.get(key).append(w)
            #Otherwise, add it to the dic
            else:
                dic[key] = [w]
        return dic.values()