class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixsum={}
        prefixsum[0]=1
        res=0
        Sum=0
        for i in nums:
            Sum+=i
            t=Sum-k
            if t in prefixsum:
                res+=prefixsum[t]
            prefixsum[Sum]=prefixsum.get(Sum,0)+1
        return res