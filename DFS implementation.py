def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neigh in graph[node]:
            dfs_recursive(graph, neigh, visited)

# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B','C'],
        'B': ['D','E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("DFS Recursive Traversal:")
    dfs_recursive(graph, 'A')
