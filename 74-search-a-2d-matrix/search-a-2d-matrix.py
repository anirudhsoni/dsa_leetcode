class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l=0
        r=len(matrix)-1
        while l<=r:
            m=(l+r)//2
            if matrix[m][0]<=target<=matrix[m][-1]:
                L=0
                R=len(matrix[m])-1
                while L<=R:
                    M=(L+R)//2
                    if matrix[m][M]==target:
                        return True
                    elif matrix[m][M]>target:
                        R=M-1
                    else:
                        L=M+1
                return False
            elif matrix[m][0]>target:
                r=m-1
            else :
                l=m+1
        return False
