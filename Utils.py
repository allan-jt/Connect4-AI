from Constants import *

#	WIN VALIDATION
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


#	OTHER UTILITIES
def swap_color(color: tuple) -> tuple:
	# Only swaps red for yellow and vice versa
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

def	get_free_spaces(board: dict, turn: tuple) -> list:
	free_spaces: list = []	# all free spaces
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

def copy_dict(board: dict) -> dict:
	copied_board = {}
	
	for key in board.keys():
		copied_board[key] = board[key]
	return copied_board

def increment(position: tuple, x_step: int, y_step: int) -> tuple:
	posX = position[X] + x_step
	posY = position[Y] + y_step
	return (posX, posY)