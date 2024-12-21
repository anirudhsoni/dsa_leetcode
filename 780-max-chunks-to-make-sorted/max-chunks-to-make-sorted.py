class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mx=0
        res=0
        for idx,val in enumerate(arr):
            mx=max(mx,val)
            if mx==idx:
                res+=1
        return res