class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={}
        for a,b in prerequisites:
            if b not in adj:
                adj[b]=[]
            adj[b].append(a)

        vst=set()
        path=set()

        def dfs(n):
            if n in path:
                return False
            if n in vst:
                return True

            vst.add(n)
            path.add(n)
            for i in adj.get(n,{}):
                if not dfs(i):
                    return False
            path.remove(n)
            return True

        # print(adj)
        for i in adj:
            if i not in vst and not dfs(i):
                return False

        return True

