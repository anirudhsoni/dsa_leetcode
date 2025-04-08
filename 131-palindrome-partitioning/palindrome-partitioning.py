class Solution:
    
    def palindromeCheck(self, s: str) -> bool:
        return s==s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        result=[]
        stack=[]
        def dfs(s):
            # print(s)
            if len(s)==0:
                result.append(stack[::])
                return
            for i in range(1,len(s)+1):
                # print(i)
                if self.palindromeCheck(s[:i]):
                    stack.append(s[:i])
                    dfs(s[i:])
                    stack.pop()
            return
        dfs(s)
        return result
        

        