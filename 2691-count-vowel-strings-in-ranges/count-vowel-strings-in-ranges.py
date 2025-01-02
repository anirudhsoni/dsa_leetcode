class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        list_start_end_with_vowel=[0]*len(words)
        leftsum=[0]
        rightsum=[]
        res=[]
        vowels={'a','e','i','o','u'}
        ls=0
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                list_start_end_with_vowel[i]=1
                ls+=1
            leftsum.append(ls)
        sm=sum(list_start_end_with_vowel)
        # rightsum.append(sm)
        for i in leftsum:
            rightsum.append(sm-i)

        # print(leftsum,rightsum)    

        for idx,val in enumerate(queries):
            res.append(sm-leftsum[val[0]]-rightsum[val[1]+1])
        return res

        