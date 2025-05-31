class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        if len(nums)==1:
            return min(abs(goal-nums[0]),abs(goal))
        nums1=nums[:len(nums)//2]
        nums2=nums[len(nums)//2:]
        dp1={0:{0,nums1[0]}}
        dp2={0:{0,nums2[0]}}

        for i in range(1,len(nums1)):
            dp1[i]={0}
            for j in dp1[i-1]:
                dp1[i].add(j)
                dp1[i].add(j+nums1[i])
        for i in range(1,len(nums2)):
            dp2[i]={0}
            for j in dp2[i-1]:
                dp2[i].add(j)
                dp2[i].add(j+nums2[i])
        

        s2=sorted(dp2[len(nums2)-1])
        ans=10**10
        # for each possible sum of the 1st half, find the sum in the 2nd half
        # that gives a value closest to the goal using binary search
        for s in dp1[len(nums1)-1]:
            remain=goal-s
			# binary search for the value in s2 that's closest to the remaining value
            i2=bisect_left(s2,remain)
            if i2<len(s2):
                ans=min(ans,abs(remain-s2[i2]))
            if i2>0:
                ans=min(ans,abs(remain-s2[i2-1]))
        return ans