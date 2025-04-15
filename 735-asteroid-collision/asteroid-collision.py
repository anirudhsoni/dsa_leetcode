class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        i=0
        while i<len(asteroids):
            if stack:
                if asteroids[i]<0:
                    while stack and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
                        stack.pop()
                    if stack and stack[-1]<0:
                        stack.append(asteroids[i])
                    elif stack and stack[-1]==abs(asteroids[i]):
                        stack.pop()
                    elif not stack:
                        stack.append(asteroids[i])
                else:
                    stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])
            i+=1
        return stack
