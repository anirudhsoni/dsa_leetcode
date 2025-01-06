class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        b=[int(i) for i in boxes]
        res=[0]*len(boxes)
        for i in range(len(res)):
            for j in range(len(b)):
                res[i]+=abs(j-i)*b[j]
        return res
        