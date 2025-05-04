class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        smallmap=[[set() for i in range(3)] for _ in range(3)]

        rowset=[set() for _ in range(9)]
        colset=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    rowset[i].add(board[i][j])
                    colset[j].add(board[i][j])
                    smallmap[i//3][j//3].add(board[i][j])
        # print(smallmap)
        # print(rowset)
        # print(colset)
        def dfs(r,c):
            if r==9:
                return True
            if c==9:
                return dfs(r+1,0)
            if board[r][c]!='.':
                return dfs(r,c+1)
            
            for _ in '123456789':
                if _ not in smallmap[r//3][c//3] and _ not in rowset[r] and _ not in colset[c]:
                    board[r][c]=_
                    smallmap[r//3][c//3].add(_)
                    rowset[r].add(_)
                    colset[c].add(_)
                    if dfs(r,c+1):
                        return True
                    board[r][c]='.'
                    smallmap[r//3][c//3].remove(_)
                    rowset[r].remove(_)
                    colset[c].remove(_)
        dfs(0,0)

        return
                
        