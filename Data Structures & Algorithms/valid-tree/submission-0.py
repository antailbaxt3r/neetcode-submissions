class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        visited = set()
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[v].append(u)
            adj[u].append(v)
        
        def dfs(node, pred):
            if node in visited:
                return False
            visited.add(node)
            for n in adj[node]:
                if n == pred:
                    continue
                if not dfs(n, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n

