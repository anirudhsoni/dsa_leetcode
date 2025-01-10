class Solution:

    def charCountArr(self,word: str) -> List[int]:
        arr=[0]*26
        for w in word:
            arr[ord(w)-ord('a')]+=1
        return arr

    def isSubstring(self,string: List[int], substring: List[int]) -> bool:
        for i in range(26):
            if substring[i]>string[i]:
                return False
        return True


    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        superSubstring=[0]*26
        for word in words2:
            for idx,val in enumerate(self.charCountArr(word)):
                if superSubstring[idx]<val:
                    superSubstring[idx]=val

        result=[]

        for word in words1:
            if self.isSubstring(self.charCountArr(word),superSubstring):
                result.append(word)
        
        return result