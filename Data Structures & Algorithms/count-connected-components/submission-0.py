class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs (x):
            q = collections.deque([x])
            visited.add(x)

            while q:
                node = q.popleft()
                for ne in adj[node]:
                    if ne not in visited:
                        visited.add(ne)
                        q.append(ne)
        answer = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                answer += 1
        return answer
