#depth-first search
def solve(game_state):
	if is_winner(game_state):
		return True
	
	for next_state in next_states:
		if solve(next_state):
			return True
	
	return False
