class Solution:
    def canPartition(self, arr: List[int]) -> bool:

        k=sum(arr)
        if k%2==0:
            k=k//2
            dp={0:{0,arr[0]}}
            for i in range(1,len(arr)):
                dp[i]={0}
                for j in dp[i-1]:
                    dp[i].add(j)
                    if j+arr[i]<=k:
                        dp[i].add(j+arr[i])
            if k in dp[len(arr)-1]:
                return True
        return False