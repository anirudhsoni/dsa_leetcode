class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        def Find(char,direction='left'):
            if direction=='left':
                for i in range(len(s)):
                    if s[i]==char:
                        return i
            else:
                for i in range(len(s)-1,-1,-1):
                    if s[i]==char:
                        return i
        
        chars=set(s)
        cnt=0
        for char in chars:
            l=Find(char,'left')
            r=Find(char,'right')
            cnt+=len(set(s[l+1:r]))
        
        return cnt

        