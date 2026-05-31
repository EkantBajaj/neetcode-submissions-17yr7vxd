class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col = len(board),len(board[0])
        def check(i,j,k):
            if k==len(word):
                return True

            if(i<0 or i>=row or j<0 or j>=col or board[i][j]!=word[k]):
                return False
            
            temp = board[i][j]
            board[i][j]="#"

            found = ( check(i+1,j,k+1) or check(i-1,j,k+1) or check(i,j+1,k+1) or check(i,j-1,k+1))

            board[i][j]=temp
            return found
        
        for i in range(row):
            for j in range(col):
                if check(i,j,0):
                    return True
        
        return False
            