class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        idx={}
        for i in range(len(arr)):
            idx[arr[i]]=i
        sArr=sorted(arr)
        pos=[]
        for i in range(len(arr)):
            a=i
            b=idx[sArr[i]]
            if a<b:
                pos.append([a,b])
            else:
                pos.append([b,a])
        pos.sort()
        res=[]
        res.append(pos[0])
        i=1
        while i<len(pos):
            # print(pos[i])
            if res[-1][-1]>=pos[i][0]:
                res[-1][-1]=max(pos[i][1],res[-1][-1])
            else:
                res.append(pos[i])
            i+=1
        # print(pos,res)
        return len(res)
