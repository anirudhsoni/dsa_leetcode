class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=set()
        def dfs(i,l,sm):
            if sm==target:
                if tuple(l) not in res:
                    res.add(tuple(l))
            if i>=len(candidates) or sm>target:
                return
            l.append(candidates[i])
            dfs(i,l,sm+candidates[i])
            l.pop()
            dfs(i+1,l,sm)
        dfs(0,[],0)
        return list(res)



        