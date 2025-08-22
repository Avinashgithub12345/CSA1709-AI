from itertools import permutations

def tsp(graph, start=0):
    n = len(graph)
    cities = range(n)
    min_path = None
    min_cost = float('inf')

    for perm in permutations([c for c in cities if c != start]):
        path = (start,) + perm + (start,)
        cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
        if cost < min_cost:
            min_cost, min_path = cost, path

    return min_cost, min_path

# Example
if __name__ == "__main__":
    # Distance matrix
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    cost, path = tsp(graph)
    print("Minimum Cost:", cost)
    print("Path:", path)
