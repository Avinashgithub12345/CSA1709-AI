# Map Coloring using Backtracking (CSP)

def is_valid(state, node, color, neighbors):
    for n in neighbors[node]:
        if state.get(n) == color:  # adjacent same color not allowed
            return False
    return True

def backtrack(state, nodes, colors, neighbors):
    if len(state) == len(nodes):   # all nodes colored
        return state
    
    node = [n for n in nodes if n not in state][0]  # unassigned node
    for color in colors:
        if is_valid(state, node, color, neighbors):
            state[node] = color
            result = backtrack(state, nodes, colors, neighbors)
            if result: 
                return result
            state.pop(node)
    return None

if __name__ == "__main__":
    # Example: Australia map (7 regions)
    nodes = ["WA","NT","SA","Q","NSW","V","T"]
    colors = ["Red","Green","Blue"]
    neighbors = {
        "WA": ["NT","SA"],
        "NT": ["WA","SA","Q"],
        "SA": ["WA","NT","Q","NSW","V"],
        "Q": ["NT","SA","NSW"],
        "NSW": ["Q","SA","V"],
        "V": ["SA","NSW"],
        "T": []
    }

    solution = backtrack({}, nodes, colors, neighbors)
    print("Solution:", solution)
