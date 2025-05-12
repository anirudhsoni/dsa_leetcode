class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        h=[]
        adj={i:set() for i in range(1,n+1)}
        for a,b,w in times:
            adj[a].add((b,w))
        
        h.append([0,k])
        vst=set()
        while h:
            time,node=heapq.heappop(h)
            if node not in vst:
                vst.add(node)
                if len(vst)==n:
                    return time
                for child,t in adj[node]:
                    heapq.heappush(h,[t+time,child])
            
        return -1
        