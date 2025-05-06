class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        moves=[[0,1],[1,0],[0,-1],[-1,0]]
        vst=set()
        q=collections.deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    q.append((i,j))
        dist=0
        inq=set()
        while q:
            dist+=1
            for i in range(len(q)):
                r,c=q.popleft()
                if (r,c) not in vst:
                    vst.add((r,c))
                    for R,C in moves:
                        if -1<r+R<len(mat) and -1<c+C<len(mat[0]):
                            if mat[r+R][c+C]>0 and (r+R,c+C) not in inq:
                                mat[r+R][c+C]=dist
                                q.append((r+R,c+C))
                                inq.add((r+R,c+C))
        return mat
                            


        