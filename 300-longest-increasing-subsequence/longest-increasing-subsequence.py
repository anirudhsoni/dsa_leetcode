class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def bleft(s,num,l,r):
            while l<r:
                m=(l+r)//2
                if s[m]<num:
                    l=m+1
                else:
                    r=m
            return (l+r)//2
        
        lis=[]

        for i in nums:
            if not lis:
                lis.append(i)
            else:
                if lis[-1]<i:
                    lis.append(i)
                else:
                    lis[bleft(lis,i,0,len(lis))]=i
        
        return len(lis)
