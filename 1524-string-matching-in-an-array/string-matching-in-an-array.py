class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        words.sort(key=len)
        # print(words)
        for w in range(len(words)):
            for word in words[w+1:]:
                if words[w] in word:
                    res.append(words[w])
                    break
        return res

        