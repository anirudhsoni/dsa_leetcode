class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj={}

        wordList.append(beginWord)

        for w in wordList:
            for i in range(len(w)):
                pattern=w[:i]+'*'+w[i+1:]
                if pattern not in adj:
                    adj[pattern]=set()
                adj[pattern].add(w)
        
        q=collections.deque()
        q.append(beginWord)
        ops=0
        vst=set()
        while q:
            ops+=1
            for _ in range(len(q)):
                pop=q.popleft()
                if pop==endWord:
                    return ops
                if pop not in vst:
                    vst.add(pop)
                    for i in range(len(pop)):
                        pattern=pop[:i]+'*'+pop[i+1:]
                        if pattern in adj:
                            for w in adj[pattern]:
                                q.append(w)
            
        return 0