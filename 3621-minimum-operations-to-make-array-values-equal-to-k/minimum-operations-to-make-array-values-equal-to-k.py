class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        l=set(nums)
        cnt=0
        less=0
        for i in l:
            if i>k:
                cnt+=1
            if i<k:
                return -1
        return cnt 