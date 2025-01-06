class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        shift_cnt=[0]*(len(s)+1)

        for shift in shifts:
            if shift[2]==1:
                shift_cnt[shift[0]]+=1
                shift_cnt[shift[1]+1]-=1
            else:
                shift_cnt[shift[0]]-=1
                shift_cnt[shift[1]+1]+=1

        def shiftChar(ch,num):
            idx=ord(ch)-ord('a')
            idx=abs((idx+num)%26)
            return chr(idx+ord('a'))
        
        res=''
        dif=0
        print(shift_cnt)
        for idx,val in enumerate(s):
            dif+=shift_cnt[idx]
            res+=shiftChar(val,dif)
        return res

        