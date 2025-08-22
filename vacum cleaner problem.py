def vacuum_cleaner(env, start):
    print("Initial State:", env, "Vacuum at", start)
    cost = 0
    loc = start

    while "Dirty" in env.values():
        if env[loc] == "Dirty":
            print("Cleaning", loc)
            env[loc] = "Clean"
            cost += 1
        else:
            print(loc, "already clean")

        # Move to the other room
        loc = "A" if loc == "B" else "B"
        cost += 1

    print("Final State:", env, "Cost =", cost)


if __name__ == "__main__":
    # Environment setup
    env = {"A": "Dirty", "B": "Dirty"}   # both rooms dirty
    vacuum_cleaner(env, "A")
