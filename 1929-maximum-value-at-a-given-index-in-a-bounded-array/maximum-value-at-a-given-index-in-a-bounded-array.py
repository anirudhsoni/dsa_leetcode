class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def getSum(idx,n,val):
            # print('calc sum for val = ',val,' for length of array ',n,' at index ',idx)
            leftN=idx+1
            rightN=n-idx
            # print(leftN,rightN)
            sm=0
            if val>leftN:
                sm+=(leftN*(val+val+1-leftN))/2
            else:
                sm+=((val*(1+val))/2)+leftN-val
            if val>rightN:
                sm+=(rightN*(val+val+1-rightN))/2
            else:
                sm+=((val*(1+val))/2)+rightN-val
            sm-=val
            # print('total sum',sm)
            return sm

        l=1
        r=maxSum
        res=1
        while l<=r:
            m=(l+r)//2
            sm=getSum(index,n,m)
            if sm<=maxSum:
                res=max(res,m)
            if sm>maxSum:
                r=m-1
            else:
                l=m+1
            
        return res
            


        