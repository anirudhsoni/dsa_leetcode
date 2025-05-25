class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def get_mx(num):
            if len(num)<3:
                return max(nums)
            num[1]=max(num[0],num[1])
            # print(num)
            for i in range(2,len(num)):
                num[i]=max(num[i-1],num[i-2]+num[i])
            return num[-1]
        
        return max(get_mx(nums[1:]),get_mx(nums[:-1]))
        