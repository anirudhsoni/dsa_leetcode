class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        rank={}
        parent={}
        nameMap={}

        def find(mail):
            if mail not in parent:
                parent[mail]=mail
            if parent[mail]==mail:
                return mail
            parent[mail]=find(parent[mail])
            return parent[mail]

        def Rank(mail):
            if mail not in rank:
                rank[mail]=1
            return rank[mail]

        def union(A,B):
            Aparent=find(A)
            Bparent=find(B)
            if Aparent!=Bparent:
                if Rank(Aparent)<Rank(Bparent):
                    rank[Bparent]+=rank[Aparent]
                    parent[Aparent]=Bparent
                else:
                    rank[Aparent]+=rank[Bparent]
                    parent[Bparent]=Aparent

        def getConnectedMails(mail):
            result=[]
            P=find(mail)
            for i in parent:
                # print(i,parent[i])
                if find(parent[i])==P:
                    # print(i)
                    result.append(i)
            return sorted(result)
        
        for arr in accounts:
            for mail in arr[2:]:
                union(arr[1],mail)

        result=[]
        vst=set()
        for arr in accounts:
            if find(arr[1]) not in vst:
                tmp=[arr[0]]+getConnectedMails(arr[1])
                vst.add(find(arr[1]))
                result.append(tmp.copy())
        # print(vst,rank,parent)
        return result
        
        
        