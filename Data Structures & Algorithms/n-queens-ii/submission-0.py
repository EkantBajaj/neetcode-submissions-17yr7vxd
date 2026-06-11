class Solution:
    def totalNQueens(self, n: int) -> int:
        cols= set()
        diag1= set()
        diag2= set()

        board = [["."]*n for _ in range(n)]
        res = []
        def generate(r):

            if r==n:
                res.append( ["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols:
                    continue
                if r-c in diag1:
                    continue
                
                if r+c in diag2:
                    continue

                cols.add(c)
                diag1.add(r-c)
                diag2.add(r+c)

                board[r][c]="Q"

                generate(r+1)

                board[r][c]="."
                cols.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)
        generate(0)
        return len(res)     