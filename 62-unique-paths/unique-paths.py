class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr=[1]*n
        for i in range(m-1):
            for j in range(1,n):
                arr[j]=arr[j]+arr[j-1]
        return arr[-1]