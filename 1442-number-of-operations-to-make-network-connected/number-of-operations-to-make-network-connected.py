class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1

        parent={i:i for i in range(n)}

        def find(a):
            # print(parent,a)
            if parent[a]==a:
                return a
            parent[a]=find(parent[a])
            return parent[a] 

        def union(a,b):
            A,B=find(a),find(b)
            if A==B:
                return
            parent[B]=A
            return

        for a,b in connections:
            union(a,b)

        cnt=0
        for i in parent:
            if parent[i]==i:
                cnt+=1
        return cnt-1

        