#Have to create a word class to compare with count and lexicographical order
#Runtime O(n log(k))
class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        #if freq are equal
        if self.freq == other.freq:
            #compare lexicographically
            return self.word > other.word
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mappings = {}
        
        #populate dic with word -> freq
        for word in words:
            if word in mappings:
                mappings[word] += 1
            else:
                mappings[word] = 1
        
        heap = []
        #print(mappings.items())
        # ^ = dict_items([('i', 2), ('love', 2), ('leetcode', 1), ('coding', 1)])
        
        for word, freq in mappings.items():
            #add word,freq to Word class created
            check = Word(word,freq)
            #if heapPQ full, pop off smallest val and add check
            if len(heap) == k:
                heappushpop(heap, check)
            else:
                heappush(heap, check)
        
        res = []
        while heap:
            res.append(heappop(heap).word)
        #return result in decreasing order
        return res[::-1]