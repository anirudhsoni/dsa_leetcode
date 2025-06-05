class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        text1=str1
        text2=str2
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
        # print(str1,str2)

        # for i in dp:
        #     print(i)

        s=''
        i=len(str1)
        j=len(str2)
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                s=str1[i-1]+s
                i-=1
                j-=1
            else:
                if dp[j-1][i]>dp[j][i-1]:
                    s=str2[j-1]+s
                    j-=1
                else:
                    s=str1[i-1]+s
                    i-=1
        if i>0:
            s=str1[:i]+s
        elif j>0:
            s=str2[:j]+s
        # print(s)
        return s