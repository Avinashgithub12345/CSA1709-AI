from collections import deque

def water_jug_problem(jug1, jug2, target):
    visited = set()  # to track visited states
    q = deque()

    # initial state (0,0)
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        print(f"({x}, {y})")  # printing the steps

        # if we reach target
        if x == target or y == target:
            print("Reached target!")
            return True

        # Possible operations:
        q.append((jug1, y))         # fill jug1
        q.append((x, jug2))         # fill jug2
        q.append((0, y))            # empty jug1
        q.append((x, 0))            # empty jug2
        q.append((min(x + y, jug1), max(0, x + y - jug1)))  # pour jug2 -> jug1
        q.append((max(0, x + y - jug2), min(x + y, jug2)))  # pour jug1 -> jug2

    print("No solution found.")
    return False


# Example: Jug1 = 4L, Jug2 = 3L, Target = 2L
water_jug_problem(4, 3, 2)
