class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums.sort()
        
        for fix in range(1,len(nums)-1):
            l=0
            r=len(nums)-1
            while l<fix and r>fix:
                sm=nums[l]+nums[fix]+nums[r]
                if sm>0:
                    r-=1
                elif sm<0:
                    l+=1
                else:
                    res.add((nums[l],nums[fix],nums[r]))
                    l+=1
                    r-=1
        return list(res)
                    