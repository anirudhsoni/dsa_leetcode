class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content=0
        gi=0
        si=0
        while gi<len(g) and si<len(s):
            if g[gi]<=s[si]:
                content+=1
                gi+=1
                si+=1
            elif g[gi]>s[si]:
                si+=1
        return content