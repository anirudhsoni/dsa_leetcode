class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache={}
        def dfs(i,sm):
            if i==len(nums) and sm==target:
                return 1
            if i==len(nums):
                return 0
            
            if (i,sm) in cache:
                return cache[(i,sm)]
            
            cache[(i,sm)] = dfs(i+1,sm+nums[i])+dfs(i+1,sm-nums[i])
        
            return cache[(i,sm)]

        return dfs(0,0)
        