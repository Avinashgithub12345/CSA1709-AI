from collections import deque

def is_valid(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if (m_left and m_left < c_left) or (m_right and m_right < c_right):
        return False
    return True

def missionaries_cannibals():
    start = (3, 3, 0, 0, 1)  # (M_left, C_left, M_right, C_right, boat_side)
    goal = (0, 0, 3, 3, 0)
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]  # possible boat moves
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (mL, cL, mR, cR, boat), path = queue.popleft()
        if (mL, cL, mR, cR, boat) == goal:
            return path
        for m, c in moves:
            if boat == 1:   # boat on left -> move to right
                new = (mL-m, cL-c, mR+m, cR+c, 0)
            else:           # boat on right -> move to left
                new = (mL+m, cL+c, mR-m, cR-c, 1)
            if is_valid(*new[:-1]) and new not in visited:
                visited.add(new)
                queue.append((new, path+[new]))
    return None

if __name__ == "__main__":
    solution = missionaries_cannibals()
    if solution:
        for step in solution:
            print(step)
    else:
        print("No solution found.")
