class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = {i:[] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visit = set()

        def dfs(v,parent):
            if v in visit:
                return False
            visit.add(v)
            for each in adj[v]:
                if each == parent:
                    continue
                if not dfs(each,v):
                    return False
            return True
        
        
        if not dfs(0,-1):
            return False
        return True if len(visit)==n else False