from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(neigh for neigh in graph[node] if neigh not in visited)

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
    print("BFS Traversal:")
    bfs(graph, 'A')
