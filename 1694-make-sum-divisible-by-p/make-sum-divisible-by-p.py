class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sm=sum(nums)
        r=sm%p
        if r == 0:
            return 0
        currentSum=0
        cache={0:-1}
        minlen=len(nums)
        for i,n in enumerate(nums):
            currentSum+=n
            currentRemainder=currentSum%p
            t=(currentRemainder-r+p)%p
            if t in cache:
                minlen=min(minlen, i-cache[t])
            cache[currentRemainder]=i
        return minlen if minlen<len(nums) else -1

        
