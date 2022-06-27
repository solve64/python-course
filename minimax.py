#minimax
def minimax(game_state,depth,max,next_move):
	if depth<=0 or is_game_over(game_state):
		return get_score(game_state)
	
	value=-999 if max else 999
	
	for next_state in next_states:
		v=minimax(next_state,depth-1,not max,None)
		
		if (max and v>value) or (not max and v<value):
			value=v
				
			if not next_move is None:
				next_move.clear()
				next_move.append(next_state)
	
	return value
