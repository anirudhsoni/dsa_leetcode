class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        l=[i for i in range(1,10)]
        res=[]
        stack=[]

        def dfs(i):
            if len(stack)==k and sum(stack)==n:
                res.append(stack.copy())
                return
            if i>=len(l) or sum(stack)>n:
                return
            stack.append(l[i])
            dfs(i+1)
            stack.pop()
            dfs(i+1)
        
        dfs(0)
        return res
        