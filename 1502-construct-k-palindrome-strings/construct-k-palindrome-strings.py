class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        arr=[0]*26
        for i in s:
            arr[ord(i)-ord('a')]+=1
        cnt=0
        for i in arr:
            if i%2==1:
                cnt+=1
        if cnt<=k:
            return True
        return False