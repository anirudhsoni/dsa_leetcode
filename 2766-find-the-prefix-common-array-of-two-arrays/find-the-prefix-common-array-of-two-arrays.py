class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        Aset={}
        Bset={}
        resdic={}
        tmp=0
        res=[]
        for i in range(len(A)):
            Aset[A[i]]=Aset.get(A[i],0)+1
            Bset[B[i]]=Bset.get(B[i],0)+1
            if A[i]==B[i]:
                tmp+=1
                res.append(tmp)
                continue
            if A[i] in Bset:
                tmp+=1
            if B[i] in Aset:
                tmp+=1
            res.append(tmp)
        return res
