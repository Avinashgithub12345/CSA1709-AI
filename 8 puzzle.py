import heapq

# Goal State
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the blank space

# Movements (up, down, left, right)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# Function to find position of blank (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Function to calculate Manhattan Distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = divmod(value - 1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance


# Convert state to tuple (for hashing in visited set)
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)


# Generate new possible states
def generate_states(state):
    x, y = find_blank(state)
    new_states = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            new_states.append(new_state)
    return new_states


# A* Algorithm
def solve_puzzle(start_state):
    pq = []
    heapq.heappush(pq, (manhattan_distance(start_state), 0, start_state, []))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal_state:
            return path + [state]

        visited.add(state_to_tuple(state))

        for new_state in generate_states(state):
            if state_to_tuple(new_state) not in visited:
                new_path = path + [state]
                h = manhattan_distance(new_state)
                heapq.heappush(pq, (g + 1 + h, g + 1, new_state, new_path))

    return None


# Print state nicely
def print_state(state):
    for row in state:
        print(row)
    print()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    # Example Start State
    start_state = [[1, 2, 3],
                   [4, 0, 6],
                   [7, 5, 8]]

    print("Start State:")
    print_state(start_state)

    solution = solve_puzzle(start_state)

    if solution:
        print("Steps to solve 8-Puzzle:")
        for step, state in enumerate(solution):
            print("Step", step)
            print_state(state)
    else:
        print("No solution found!")
