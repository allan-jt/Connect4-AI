from Utils import *

def	minimax(board: dict, turn: tuple, alpha: float, beta: float,
	depth: int = DEPTH) -> tuple:

	available_spaces = get_free_spaces(copy_dict(board), turn)
#	print(depth, " ", available_spaces)
	if len(available_spaces) == 1: # Base case
		return available_spaces[0]
	
	ideal_position: tuple = available_spaces[0]
	if turn == RED:	# maximizing player (computer)
		max_val = -INFINITY
		for space in available_spaces:
			value = speculate(copy_dict(board), space, turn, alpha, beta, depth - 1)
		#	print("alpha: ", alpha, " value: ", value, " max_val: ", max_val)
			if value > max_val:
				max_val = value
				ideal_position = space
			alpha = max(alpha, value)
		#	print("alpha: ", alpha)
			if beta <= alpha:
				break
	else:			# minimizing player (human)
		min_val = INFINITY
		for space in available_spaces:
			value = speculate(copy_dict(board), space, turn, alpha, beta, depth - 1)
		#	print("beta: ", beta, " value: ", value, " min_val: ", min_val)
			if value < min_val:
				min_val = value
				ideal_position = space
			beta = min(beta, value)
		#	print("beta: ", beta)
			if beta <= alpha:
				break
	
	return ideal_position

def	speculate(board: dict, position: tuple, turn: tuple, 
	alpha: float, beta: float, depth) -> float:
	
	board[position] = turn
	temp_turn = turn	
	
	if (not check_win(board, position, temp_turn) 
		and spaces_left(board) > 0 and depth > 0):
		temp_turn = swap_color(temp_turn)		
		position = minimax(copy_dict(board), temp_turn, alpha, beta, depth)
		board[position] = temp_turn
	
	return calculate_score(board)