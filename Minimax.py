from Utils import *
from copy import deepcopy

def	minimax(board: dict, turn: tuple, alpha: float, beta: float) -> tuple:
	available_spaces = get_free_spaces(deepcopy(board), turn)
	if len(available_spaces) == 1: # Base case
		return available_spaces[0]
	
	ideal_position: tuple = available_spaces[0]
	if turn == RED:	# maximizing player (computer)
		max_val = -INFINITY
		for space in available_spaces:
			value = speculate(deepcopy(board), deepcopy(space),
				deepcopy(turn), alpha, beta)
		#	print("alpha: ", alpha, " value: ", value, " max_val: ", max_val)
			if value > max_val:
				max_val = value
				ideal_position = space
			alpha = max(alpha, max_val)
		#	print("alpha: ", alpha)
			if beta <= alpha:
				break
	else:			# minimizing player (human)
		min_val = INFINITY
		for space in available_spaces:
			value = speculate(deepcopy(board), deepcopy(space),
				deepcopy(turn), alpha, beta)
		#	print("beta: ", beta, " value: ", value, " min_val: ", min_val)
			if value < min_val:
				min_val = value
				ideal_position = space
			beta = min(beta, min_val)
		#	print("beta: ", beta)
			if beta <= alpha:
				break
	
	return ideal_position

def	speculate(board: dict, position: tuple, turn: tuple, 
	alpha: float, beta: float) -> float:
	
	board[position] = turn
	temp_turn = turn
	while not check_win(board, position, temp_turn):
		if spaces_left(board) == 0:
			return 0
		temp_turn = swap_color(temp_turn)		
		position = minimax(deepcopy(board), deepcopy(temp_turn),
			alpha, beta)
		board[position] = temp_turn
	
	percent_left = 100 * spaces_left(board) / (GAME_HEIGHT * GAME_WIDTH)
	score = percent_left + 1
	if temp_turn == YELLOW:
		score *= -1
	return score