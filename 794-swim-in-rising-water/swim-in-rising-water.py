class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        moves=[[0,1],[1,0],[-1,0],[0,-1]]
        h=[]
        heapq.heappush(h,[grid[0][0],[0,0]])
        time=float('-infinity')
        vst=set()
        while h:
            # print(h)
            popped=heapq.heappop(h)
            time=max(time,popped[0])
            # print(time)
            if popped[1]==[len(grid)-1,len(grid)-1]:
                return time
            if tuple(popped[1]) not in vst:
                vst.add(tuple(popped[1]))
                for r,c in moves:
                    R=r+popped[1][0]
                    C=c+popped[1][1]
                    if -1<R<len(grid) and -1<C<len(grid):
                        heapq.heappush(h,[grid[R][C],[R,C]])
        return time

