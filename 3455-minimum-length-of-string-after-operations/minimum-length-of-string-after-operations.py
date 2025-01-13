class Solution:
    def minimumLength(self, s: str) -> int:

        arr=[0]*26

        for i in s:
            arr[ord(i)-ord('a')]+=1
        
        for i in range(26):
            if arr[i]%2==1:
                arr[i]=1
            elif arr[i]!=0 and arr[i]%2==0:
                arr[i]=2
        
        return sum(arr)
        