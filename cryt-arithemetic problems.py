from itertools import permutations

def solve(puzzle):
    letters = sorted(set(puzzle.replace(" ", "")) - set("+=*-/()"))
    for perm in permutations("0123456789", len(letters)):
        m = dict(zip(letters, perm))
        if any(m[w[0]] == "0" for w in puzzle.split() if w.isalpha()): continue
        eq = puzzle.translate(str.maketrans(m))
        try:
            if eval(eq): return eq, m
        except: pass

print(solve("SEND+MORE==MONEY"))
