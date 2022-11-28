from Scoring import *

def	minimax(board: dict, turn: tuple, alpha: float, beta: float,
	depth: int = DEPTH) -> tuple:

	available_spaces = get_free_spaces(copy_dict(board), turn)
#	print(depth, " ", available_spaces)
	if len(available_spaces) == 1: # Base case
		board[available_spaces[0]] = turn
		return available_spaces[0], calculate_score(board, turn)
	
	ideal_position: tuple = available_spaces[0]
	if turn == RED:	# maximizing player (computer)
		max_val = -INFINITY
		for space in available_spaces:
			board[space] = turn
			value = 0
			position = ()

			if depth > 0 and not check_win(board, space, turn):
				position, value = minimax(copy_dict(board), swap_color(turn), alpha, beta, depth - 1)
			else:
				position = space
				value = calculate_score(board, turn)

			board[space] = WHITE
			if value > max_val:
				max_val = value
				ideal_position = space
			alpha = max(alpha, value)
			if beta <= alpha:
				break
	else:			# minimizing player (human)
		min_val = INFINITY
		for space in available_spaces:
			board[space] = turn
			value = 0
			position = ()

			if depth > 0 and not check_win(board, space, turn):
				position, value = minimax(copy_dict(board), swap_color(turn), alpha, beta, depth - 1)
			else:
				position = space
				value = calculate_score(board, turn)

			board[space] = WHITE
		#	print("beta: ", beta, " value: ", value, " min_val: ", min_val)
			if value < min_val:
				min_val = value
				ideal_position = space
			beta = min(beta, value)
		#	print("beta: ", beta)
			if beta <= alpha:
				break
	
	if (turn == RED):
		return ideal_position, max_val
	return ideal_position, min_val

def	speculate(board: dict, position: tuple, turn: tuple, 
	alpha: float, beta: float, depth) -> float:
	
	board[position] = turn
	
	temp_turn = turn	
	if (not check_win(board, position, temp_turn) 
		and spaces_left(board) > 0 and depth > 0):
		temp_turn = swap_color(temp_turn)		
		position = minimax(copy_dict(board), temp_turn, alpha, beta, depth)
		board[position] = temp_turn
	
	return calculate_score(board, turn)