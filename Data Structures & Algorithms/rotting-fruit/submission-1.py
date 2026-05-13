class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        distance = [(1,0),(-1,0),(0,-1),(0,1)]
        visit = set()
        q = deque()
        def addRottenFruit(r,c):
            if min(r,c)<0 or r==row or c==col or (r,c) in visit or grid[r][c]==0:
                return
            q.append([r,c])
            visit.add((r,c))
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    q.append([r,c])
                    visit.add((r,c))
        
        minutes = -1
        while q:
            minutes += 1
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c]="#"
                for dr,dc in distance:
                    addRottenFruit(r+dr,c+dc)

        maxTime=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    return -1
        return minutes if minutes>0 else 0