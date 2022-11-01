class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        #combo of character and words that are possible
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        visited = {beginWord: True}
        
        #add queue and count to a queue
        q = collections.deque([[beginWord, 1]])
        #print(all_combo_dict)
        while q:
            #grab word and curr length
            word, count = q.popleft()
            if word == endWord:
                return count
            
            for i in range(len(beginWord)):
                #create word with * in it
                int_word = word[:i] + "*" + word[i+1:]
                #go through the potential words in all_combo_dict
                for nxt_word in all_combo_dict[int_word]:
                    #if the potential word has not been seen
                    if nxt_word not in visited:
                        visited[nxt_word] = True
                        #go to next word
                        q.append((nxt_word, count+1))
        return 0