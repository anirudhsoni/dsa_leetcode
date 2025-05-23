class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stack=[]
        res=[]
        def dfs(i):
            if i==len(nums):
                res.append(stack.copy())
                return
            stack.append(nums[i])
            dfs(i+1)
            stack.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res
