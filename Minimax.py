from Scoring import *

def	minimax(board: dict, turn: tuple, alpha: float, beta: float,
	depth: int = DEPTH) -> tuple:

	available_spaces = get_free_spaces(copy_dict(board), turn)
	if len(available_spaces) == 1: # Base case
		board[available_spaces[0]] = turn
		return available_spaces[0], calculate_score(board, turn)
	
	ideal_position: tuple = available_spaces[0]
	if turn == RED:	# maximizing player (computer)
		max_val = -INFINITY
		for space in available_spaces:
			position, value = speculate(board, turn, alpha, beta, depth, space)
			if value > max_val:
				max_val = value
				ideal_position = space
			alpha = max(alpha, value)
			if beta <= alpha:
				break
	else:			# minimizing player (human)
		min_val = INFINITY
		for space in available_spaces:
			position, value = speculate(board, turn, alpha, beta, depth, space)
			if value < min_val:
				min_val = value
				ideal_position = space
			beta = min(beta, value)
			if beta <= alpha:
				break
	
	if (turn == RED):
		return ideal_position, max_val
	return ideal_position, min_val

def	speculate(board: dict, turn: tuple, alpha: float, beta: float,
	depth: int, space):
	
	board[space] = turn
	if depth > 0 and not check_win(board, space, turn):
		position, value = minimax(copy_dict(board), swap_color(turn),
			alpha, beta, depth - 1)
	else:	# Stop minimax when depth = 0 or position leads to win
		position = space
		value = calculate_score(board, turn)
	board[space] = WHITE

	return position, value