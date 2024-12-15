class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s)==0:
            return 0
        Map={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        i=0
        sign=None
        while i<len(s):
            if s[i]==' ':
                i+=1
                continue
            if s[i]=='-' or s[i]=='+':
                sign=s[i]
                i+=1
                break
            if s[i] in Map:
                break
            break
        
        def dfs(i,num):
            if i>=len(s) or s[i] not in Map or num>2**31:
                return num
            num=num*10 + Map[s[i]]
            return dfs(i+1,num)
        
        n=dfs(i,0)
        if sign=='-':
            n*=-1
        if n<-2**31:
            return -2**31
        if n>2**31-1:
            return 2**31-1
        return n

