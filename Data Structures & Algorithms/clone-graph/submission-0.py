"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        n_list = []
        copy = {}

        def bfs (node):
            if node in copy:
                return copy[node]

            new_node = Node(node.val)
            copy[node] = new_node

            for n in node.neighbors:
                new_node.neighbors.append(bfs(n))
            return new_node

        return bfs(node) if node else None