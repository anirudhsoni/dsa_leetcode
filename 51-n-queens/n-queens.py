class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        r=set()
        c=set()
        sm=set()
        dif=set()
        res=[]
        b=[['.']*n for i in range(n)]
        def chk(x,y):
            if x in r or y in c or x+y in sm or x-y in dif:
                return False
            return True

        def dfs(x,y):
            if len(r)==n:
                t=[]
                for i in b:
                    t.append(''.join(i))
                res.append(t)
                return
            if x>=n:
                return
            if y==n:
                dfs(x+1,0)
                return
            if chk(x,y):
                b[x][y]='Q'
                # print(x,y,'Q')
                r.add(x)
                c.add(y)
                sm.add(x+y)
                dif.add(x-y)
                dfs(x,y+1)
                b[x][y]='.'
                r.remove(x)
                c.remove(y)
                sm.remove(x+y)
                dif.remove(x-y)
            dfs(x,y+1)
            return 
        
        dfs(0,0)
        return res

