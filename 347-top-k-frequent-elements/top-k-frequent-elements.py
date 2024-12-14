import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt=collections.Counter(nums)
        h=[]
        for i in cnt:
            heapq.heappush(h,(cnt[i],i))
            if len(h)>k:
                heapq.heappop(h)
        res=[]
        for i in h:
            res.append(i[1])
        return res