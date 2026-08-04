class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for [x, y] in prerequisites:
            adj[x].append(y)
            degree[y] += 1
            
        q = collections.deque()
        for n in range(numCourses):
            if degree[n] == 0:
                q.append(n)

        finished = 0
        while q:
            n = q.popleft()
            finished += 1
            for node in adj[n]:
                degree[node] -= 1
                if degree[node] == 0:
                    q.append(node)
        return finished == numCourses
        