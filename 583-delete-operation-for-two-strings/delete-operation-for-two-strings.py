class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        text1=word1
        text2=word2
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
        return len(text1)+len(text2)-2*dp[-1][-1]