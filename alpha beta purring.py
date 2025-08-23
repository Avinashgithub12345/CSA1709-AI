import math

# Alpha-Beta Pruning implementation
def alpha_beta_pruning(node_index, depth, is_maximizing_player, values, alpha, beta, max_depth):
    # Base condition: leaf node is reached
    if depth == max_depth:
        return values[node_index]

    if is_maximizing_player:
        best = -math.inf

        # Recurse for left and right children
        for i in range(2):
            val = alpha_beta_pruning(node_index * 2 + i, depth + 1, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        # Recurse for left and right children
        for i in range(2):
            val = alpha_beta_pruning(node_index * 2 + i, depth + 1, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best


# Example usage
if __name__ == "__main__":
    # Leaf nodes of the game tree (e.g., evaluation scores of end game states)
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    max_depth = 3  # Depth of the game tree

    best_value = alpha_beta_pruning(0, 0, True, values, -math.inf, math.inf, max_depth)
    print("The optimal value is:", best_value)
