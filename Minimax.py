from Constants import *
from copy import deepcopy

def	minimax(board: dict, turn: tuple, alpha: float, beta: float) -> tuple:
	available_spaces = get_free_spaces(board)
	if len(available_spaces) == 1: # Base case
		return available_spaces[0]
	
	ideal_position: tuple = available_spaces[0]
	if turn == RED:	# maximizing player (computer)
		max_val = -INFINITY
		for space in available_spaces:
			value = speculate(deepcopy(board), deepcopy(space),
				deepcopy(turn), deepcopy(alpha), deepcopy(beta))
			if value > max_val:
				max_val = value
				ideal_position = space
			alpha = max(alpha, max_val)
			if beta <= alpha:
				break
	else:			# minimizing player (human)
		min_val = INFINITY
		for space in available_spaces:
			value = speculate(deepcopy(board), deepcopy(space),
				deepcopy(turn), alpha, beta)
			if value < min_val:
				min_val = value
				ideal_position = space
			beta = min(beta, min_val)
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

#	VALIDATE WIN
def	check_win(board: dict, move: tuple, turn: tuple) -> bool:
	return (check_orthogonal_win(board, move, turn) 
		 or check_diagonal_win(board, move, turn))

def check_orthogonal_win(board: dict, move: tuple, turn: tuple) -> bool:
	counter = 0	# check horizontal
	for width in range(GAME_WIDTH):
		if board[(width, move[Y])] != turn:
			counter = 0
		elif (counter := counter + 1) >= WIN:
			return True

	counter = 0 # check vertical
	for height in range(GAME_HEIGHT):
		if board[(move[X], height)] != turn:
			counter = 0
		elif (counter := counter + 1) >= WIN:
			return True

	return False

def	check_diagonal_win(board: dict, move: tuple, turn: tuple) -> bool:
	counter = 1	# check / diagonal
	posX = move[X]
	posY = move[Y]
	while same_color(board, (posX := posX + 1, posY := posY + 1), turn):
		if (counter := counter + 1) >= WIN:
			return True
	posX = move[X]
	posY = move[Y]
	while same_color(board, (posX := posX - 1, posY := posY - 1), turn):
		if (counter := counter + 1) >= WIN:
			return True

	counter = 1	# check \ diagonal
	posX = move[X]
	posY = move[Y]
	while same_color(board, (posX := posX + 1, posY := posY - 1), turn):
		if (counter := counter + 1) >= WIN:
			return True
	posX = move[X]
	posY = move[Y]
	while same_color(board, (posX := posX - 1, posY := posY + 1), turn):
		if (counter := counter + 1) >= WIN:
			return True

	return False

#	UTILS
def swap_color(color: tuple) -> tuple:
	if color == YELLOW:
		return RED
	if color == RED:
		return YELLOW
	return color

def	spaces_left(board: dict) -> int:
	spaces = 0
	for space in board.values():
		if space == WHITE:
			spaces += 1
	return spaces

def	get_free_spaces(board: dict) -> list:
	free_spaces: list = []
	for width in range(GAME_WIDTH):
		for height in range(GAME_HEIGHT - 1, -1, -1):
			if board[(width, height)] == WHITE:
				free_spaces.append((width, height))
				break
	return free_spaces

def	within_bounds(positionX: int, positionY: int) -> bool:
	return (0 <= positionX < GAME_WIDTH 
		and 0 <= positionY < GAME_HEIGHT)

def	same_color(board: dict, position: tuple, color: tuple) -> bool:
	return (within_bounds(position[X], position[Y])
		and board[position] == color)