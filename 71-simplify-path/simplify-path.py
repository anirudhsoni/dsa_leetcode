class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        i=0
        while i<len(path):
            j=i+1
            while j<len(path) and path[j]!='/':
                j+=1
            w=path[i+1:j]
            if w=='..' and stack:
                stack.pop()
            elif w!='.' and w!='' and w!='..':
                stack.append(w)
            i=j
        return '/'+'/'.join(stack)