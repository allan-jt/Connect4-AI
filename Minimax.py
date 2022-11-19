from Constants import *
from copy import deepcopy

def	minimax(pieces: dict, turn: tuple, alpha: float, beta: float) -> tuple:
	available_pieces = get_free_pieces(pieces)
	if len(available_pieces) == 1: # Base case
		return available_pieces[0].position
	
	ideal_position: tuple = available_pieces[0].position
	if turn == RED:	# maximizing player (computer)
		max_val = float('-inf')
		for piece in available_pieces:
			value = speculate(pieces, piece.position, turn, alpha, beta)
			alpha = max(alpha, value)
			if value > max_val:
				max_val = value
				ideal_position = piece.position
			if beta <= alpha:
				break
	else:			# minimizing player (human)
		min_val = float('inf')
		for piece in available_pieces:
			value = speculate(pieces, piece.position, turn, alpha, beta)
			beta = min(beta, value)
			if value < min_val:
				min_val = value
				ideal_position = piece.position
			if beta <= alpha:
				break

	return ideal_position

def	speculate(pieces: dict, position: tuple, turn: tuple, 
	alpha: float, beta: float) -> float:
	
	pieces[position].color = turn
	if not check_win(pieces, position, turn):
		minimax(pieces, swap_color(turn), alpha, beta)
	
	percent_left = 100 * spaces_left(pieces) / (GAME_HEIGHT * GAME_WIDTH)
	if turn == YELLOW:
		percent_left *= -1
	
	return percent_left

#	VALIDATE WIN
def	check_win(all_pieces: dict, move: tuple, turn: tuple) -> bool:
	return (check_orthogonal_win(all_pieces, move, turn) 
		 or check_diagonal_win(all_pieces, move, turn))

def check_orthogonal_win(all_pieces: dict, move: tuple, turn: tuple) -> bool:
	counter = 0	# check horizontal
	for width in range(GAME_WIDTH):
		if all_pieces[(width, move[Y])].color != turn:
			counter = 0
		elif (counter := counter + 1) >= WIN:
			return True

	counter = 0 # check vertical
	for height in range(GAME_HEIGHT):
		if all_pieces[(move[X], height)].color != turn:
			counter = 0
		elif (counter := counter + 1) >= WIN:
			return True

	return False

def	check_diagonal_win(pieces: dict, move: tuple, turn: tuple) -> bool:
	counter = 1	# check / diagonal
	posX = move[X]
	posY = move[Y]
	while same_color(pieces, (posX := posX + 1, posY := posY + 1), turn):
		if (counter := counter + 1) >= WIN:
			return True
	posX = move[X]
	posY = move[Y]
	while same_color(pieces, (posX := posX - 1, posY := posY - 1), turn):
		if (counter := counter + 1) >= WIN:
			return True

	counter = 1	# check \ diagonal
	posX = move[X]
	posY = move[Y]
	while same_color(pieces, (posX := posX + 1, posY := posY - 1), turn):
		if (counter := counter + 1) >= WIN:
			return True
	posX = move[X]
	posY = move[Y]
	while same_color(pieces, (posX := posX - 1, posY := posY + 1), turn):
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

def	spaces_left(pieces: dict) -> int:
	spaces = 0
	for piece in pieces.values():
		if piece.color == WHITE:
			spaces += 1
	return spaces

def	get_free_pieces(pieces: dict) -> list:
	free_pieces: list = []
	for width in range(GAME_WIDTH):
		for height in range(GAME_HEIGHT - 1, -1, -1):
			piece = pieces[(width, height)]
			if piece.color == WHITE:
				free_pieces.append(piece)
				break
	return free_pieces

def	within_bounds(positionX: int, positionY: int) -> bool:
	return (0 <= positionX < GAME_WIDTH 
		and 0 <= positionY < GAME_HEIGHT)

def	same_color(all_pieces: dict, position: tuple, color: tuple) -> bool:
	return (within_bounds(position[X], position[Y])
		and all_pieces[position].color == color)