class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}

        def getSign(s):
            sign=[0]*26
            for i in s:
                sign[ord(i)-ord('a')]+=1
            return tuple(sign)

        for s in strs:
            sign=getSign(s)
            if sign in d:
                d[sign].append(s)
            else:
                d[sign]=[s]
        
        res=[]
        for key in d:
            res.append(d[key])
        return res
        