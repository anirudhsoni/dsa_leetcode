from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        moves=[[0,1],[1,0],[0,-1],[-1,0]]
        rotten=deque()
        visited=set()
        rottenCnt=0
        freshCnt=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    freshCnt+=1
                elif grid[r][c]==2:
                    rottenCnt+=1
                    rotten.append([r,c])
                    visited.add((r,c))
        time=-1
        while rotten:
            print(rotten)
            for _ in range(len(rotten)):
                R,C=rotten.popleft()
                for r,c in moves:
                    if -1<R+r<len(grid) and -1<C+c<len(grid[0]) and grid[R+r][C+c]==1:
                        grid[R+r][C+c]=2
                        rotten.append([R+r,C+c])
                        rottenCnt+=1
                        freshCnt-=1
            time+=1
        if time==-1 and freshCnt==0:
            return 0
        return time if freshCnt==0 else -1

        