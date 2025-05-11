class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        h=[]
        moves=[[0,1],[1,0],[0,-1],[-1,0]]
        res=0
        h.append([0,0,0])
        vst=set()
        absDif=0
        while h:
            d,r,c=heapq.heappop(h)
            absDif=max(absDif,d)
            if r==len(heights)-1 and c==len(heights[0])-1:
                return absDif
            vst.add((r,c))
            for R,C in moves:
                if r+R in range(len(heights)) and c+C in range(len(heights[0])) and (r+R,c+C) not in vst:
                    dif=abs(heights[r][c]-heights[r+R][c+C])
                    heapq.heappush(h,[dif,r+R,c+C])

        return absDif


        