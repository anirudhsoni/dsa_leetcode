class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp=[[-1 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        
        for i in range(len(text1)+1):
            dp[0][i]=0
        for i in range(len(text2)+1):
            dp[i][0]=0

        for idx1 in range(1,len(text2)+1):
            for idx2 in range(1,len(text1)+1):
                if text1[idx2-1]==text2[idx1-1]:
                    dp[idx1][idx2]=1+dp[idx1-1][idx2-1]
                else:
                    # print(idx1,idx2,dp)
                    dp[idx1][idx2]=max(dp[idx1][idx2-1],dp[idx1-1][idx2])
        return dp[-1][-1]
