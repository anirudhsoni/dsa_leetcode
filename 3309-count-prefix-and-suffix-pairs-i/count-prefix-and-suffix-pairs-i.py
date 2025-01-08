class Solution:
    
    def isPrefixAndSuffix(self, str1 : str, str2 : str) -> bool:
        if len(str1)>len(str2):
            return False
        if str2[:len(str1)]==str1 and str1==str2[-len(str1):]:
            return True
        return False

    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        cnt=0

        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if self.isPrefixAndSuffix(words[i],words[j]):
                    cnt+=1
        
        return cnt
        