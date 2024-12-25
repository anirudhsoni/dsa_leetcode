class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # adj={i:[] for i in range(len(graph))}
        res=[]
        path=[]
        def dfs(i):
            if i==len(graph)-1:
                res.append(path.copy())
                return
            if graph[i]==[]:
                return
            for node in graph[i]:
                path.append(node)
                dfs(node)
                path.pop()
            return
        path.append(0)
        dfs(0)
        return res