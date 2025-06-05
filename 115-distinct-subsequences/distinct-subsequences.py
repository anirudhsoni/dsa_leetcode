class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache={}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if j==len(t):
                return 1
            if i>=len(s):
                return 0
            tmp=0
            if s[i]==t[j]:
                tmp=dfs(i+1,j+1)
            tmp+=dfs(i+1,j)
            cache[(i,j)]=tmp
            return tmp
        return dfs(0,0)