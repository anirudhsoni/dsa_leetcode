class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        def dfs(o,c):
            if o==c==n:
                res.append(''.join(stack))
                return
            if o>c and o<=n:
                stack.append(')')
                dfs(o,c+1)
                stack.pop()
            if o<n and o>=c:
                stack.append('(')
                dfs(o+1,c)
                stack.pop()

        dfs(0,0)
        return res
            
