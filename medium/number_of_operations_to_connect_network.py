class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < (n-1):
            return -1

        visited = [False] * n
        islands = 0
        graph = {i:[] for i in range(n)}

        def dfs(node, visited):
            visited[node] = True
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    dfs(neighbour, visited)

        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])

        for node in range(n):
            if not visited[node]:
                islands += 1
                dfs(node, visited)
        return islands - 1
        
        