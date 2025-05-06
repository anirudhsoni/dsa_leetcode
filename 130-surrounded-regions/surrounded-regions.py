class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        moves=[[0,1],[1,0],[0,-1],[-1,0]]
        
        def dfs(r,c):
            if board[r][c]=='#' or board[r][c]=="X":
                return
            board[r][c]='#'
            for R,C in moves:
                if -1<r+R<len(board) and -1<c+C<len(board[0]):
                    dfs(r+R,c+C)
            return

        for r in range(len(board)):
            for c in range(len(board[0])):
                if r==0 or c==0 or r==len(board)-1 or c==len(board[0])-1:
                    # print(r,c)
                    dfs(r,c)
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=="O":
                    board[r][c]="X"

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=="#":
                    board[r][c]="O"
            

        