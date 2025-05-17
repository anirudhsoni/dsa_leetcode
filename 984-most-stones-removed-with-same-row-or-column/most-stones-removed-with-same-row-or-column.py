class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        parent={}
        rank={}
        
        def getRank(n):
            if n not in rank:
                rank[n]=1
            return rank[n]

        def find(n):
            if n not in parent:
                parent[n]=n
            if parent[n]==n:
                return n
            parent[n]=find(parent[n])
            return parent[n]


        def union(r,c):
            R=find(r)
            C=find(c+10000+2)
            if R!=C:
                if getRank(R)<getRank(C):
                    parent[R]=C
                    rank[C]+=rank[R]
                else:
                    parent[C]=R
                    rank[R]+=rank[C]
        
        for stone in stones:
            union(stone[0],stone[1])
        
        grps=0

        for i in parent:
            if i==find(parent[i]):
                grps+=1
        
        return len(stones)-grps



            
            
        