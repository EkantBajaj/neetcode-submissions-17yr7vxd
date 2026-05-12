class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        row,col = len(grid),len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c]==0:
                return 0
            
            res =1
            grid[r][c]= 0
            for dr,dc in directions:
                res+=dfs(r+dr,c+dc)
            return res
        def bfs(r,c):
            q=deque([(r,c)])
            res = 0
            while q:
                r,c = q.popleft()
                if r<0 or c<0 or r>=row or c>=col or grid[r][c]==0:
                    continue
                res+=1
                grid[r][c]=0
                for dr,dc in directions:
                    q.append((r+dr,c+dc))
            return res
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    res = max(res,bfs(r,c))
        
        return res