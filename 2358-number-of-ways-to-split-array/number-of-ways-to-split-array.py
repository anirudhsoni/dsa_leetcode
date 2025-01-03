class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sm=sum(nums)
        lsm=0
        cnt=0
        for i in range(len(nums)-1):
            lsm+=nums[i]
            rsm=sm-lsm
            if lsm>=rsm:
                cnt+=1
        return cnt