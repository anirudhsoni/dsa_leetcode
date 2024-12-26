class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        subs={}
        ln=len(s)//k
        for i in range(0,len(s),ln):
            subs[tuple(s[i:i+ln])]=subs.get(tuple(s[i:i+ln]),0)+1
        for i in range(0,len(s),ln):
            if tuple(t[i:i+ln]) not in subs or subs[tuple(t[i:i+ln])]==0:
                return False
            else:
                subs[tuple(t[i:i+ln])]-=1
        return True
