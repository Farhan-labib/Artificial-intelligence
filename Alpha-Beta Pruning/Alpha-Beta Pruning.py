#PART - 1

def minimax(depth, is_max, alpha, beta):
    if depth == 0:
        if is_max:
            return -1  
        else:
            return 1  

    if is_max:
        max_eval = float('-inf')
        for child in [-1, 1]:
            eval = minimax(depth - 1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in [-1, 1]:
            eval = minimax(depth - 1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def simulate_mortal_kombat(first_player):
    rounds_played = 0
    scorpion_wins = 0
    sub_zero_wins = 0
    current_player = first_player
    round_winners = []
    
    while scorpion_wins < 3 and sub_zero_wins < 3:
        alpha = float('-inf')
        beta = float('inf')
        
        winner = minimax(5, current_player == 1, alpha, beta)
        
        if winner == -1:
            round_winners.append("Scorpion")
            scorpion_wins += 1
        else:
            round_winners.append("Sub-Zero")
            sub_zero_wins += 1
        
        rounds_played += 1
        current_player = 1 - current_player
    
    if scorpion_wins > sub_zero_wins:
        game_winner = "Scorpion"
    else:
        game_winner = "Sub-Zero"
    
    return game_winner, rounds_played, round_winners

first_player = int(input("Enter the first player (0 for Scorpion, 1 for Sub-Zero): "))
game_winner, total_rounds, round_winners = simulate_mortal_kombat(first_player)

print(f"Game Winner: {game_winner}")
print(f"Total Rounds Played: {total_rounds}")
for i, winner in enumerate(round_winners, 1):
    print(f"Winner of Round {i}: {winner}")



#PART - 2
print("\nPART - 2")
def alpha_beta_pruning():
    scores = [[3, 6], [2, 3], [7, 1], [2, 0]]
    alpha, beta = float('-inf'), float('inf')

    left_1 = max(scores[0])
    if left_1 < beta:
        beta = left_1
    left_2 = max(scores[1])
    left_subtree = min(left_1, left_2)
    if left_subtree > alpha:
        alpha = left_subtree
    if alpha >= beta:
        return alpha

    right_1 = max(scores[2])
    if right_1 < beta:
        beta = right_1
    right_2 = max(scores[3])
    right_subtree = min(right_1, right_2)
    if right_subtree > alpha:
        alpha = right_subtree
    if alpha >= beta: 
        return alpha

    return max(left_subtree, right_subtree)



def pacman_game_with_pruning(c):
    scores = [[3, 6], [2, 3], [7, 1], [2, 0]]
    left_subtree = min(max(scores[0]), max(scores[1]))
    right_subtree = min(max(scores[2]), max(scores[3]))
    pacman_minimax = max(left_subtree, right_subtree)
    left_with_magic = max(max(scores[0]) - c, left_subtree)
    right_with_magic = max(max(scores[2]) - c, right_subtree)
    
    root_value = alpha_beta_pruning()

    if left_with_magic > pacman_minimax or right_with_magic > pacman_minimax:
        magic_benefit = "Using dark magic is beneficial for Pac-Man."
    else:
        magic_benefit = "Using dark magic is not beneficial for Pac-Man."

    if left_with_magic >= right_with_magic and left_with_magic > pacman_minimax:
        result = f"The new minimax value is {left_with_magic}. Pac-Man goes left and uses dark magic."
    elif right_with_magic > left_with_magic and right_with_magic > pacman_minimax:
        result = f"The new minimax value is {right_with_magic}. Pac-Man goes right and uses dark magic."
    else:
        result = f"The minimax value is {pacman_minimax}. Pac-Man does not use dark magic."
    
    result += f"\nThe final value of the root node without dark magic is {root_value}."
    result += f"\n{magic_benefit}"
    return result


# Test cases
print(pacman_game_with_pruning(2))
print(pacman_game_with_pruning(5))
