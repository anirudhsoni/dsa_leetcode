class Solution:
    def isValid(self, s: str) -> bool:
        mp={'(':')','{':'}','[':']'}
        stack=[]
        for i in s:
            if i in mp:
                stack.append(i)
            elif stack and mp[stack[-1]]==i:
                stack.pop()
            else:
                return False
        return True if not stack else False