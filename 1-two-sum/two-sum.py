class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i,v in enumerate(nums):
            if target-v in s:
                return [s[target-v],i]
            else:
                s[v]=i
        return

        