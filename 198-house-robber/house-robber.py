class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)

        nums[1]=max(nums[1],nums[0])
        
        for i in range(2,len(nums)):
            nums[i]=nums[i]+nums[i-2]
            nums[i]=max(nums[i],nums[i-1])
        
        return nums[-1]