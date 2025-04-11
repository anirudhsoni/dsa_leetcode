class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        comb=[["."]*n for i in range(n)]
        col=set()
        smset=set()
        difset=set()

        def chk(r,i):
            if i==n:
                r=[''.join(k) for k in comb]
                res.append(r)
                return 
            for c in range(n):
                if c in col or r+c in smset or r-c in difset:
                    continue
                comb[r][c]='Q'
                col.add(c)
                smset.add(r+c)
                difset.add(r-c)
                chk(r+1,i+1)
                comb[r][c]='.'
                col.remove(c)
                smset.remove(r+c)
                difset.remove(r-c)
        
        chk(0,0)
        # print(res)
        return res



            
        