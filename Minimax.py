from Constants import *
import random

#	UTILS
def swapColor(color: tuple) -> tuple:
	if color == YELLOW:
		return RED
	if color == RED:
		return YELLOW
	return color

def	spaces_left(all_pieces: dict) -> int:
	spaces = 0
	for piece in all_pieces.values():
		if piece.color == WHITE:
			spaces += 1
	return spaces

def	within_bounds(positionX: int, positionY: int) -> bool:
	return (positionX < GAME_WIDTH and positionY < GAME_HEIGHT
		and positionX >= 0 and positionY >= 0)

def	same_color(all_pieces: dict, position: tuple, color: tuple) -> bool:
	return (within_bounds(position[X], position[Y])
		and all_pieces[position].color == color)

#	VALIDATE WIN
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

def	check_win(all_pieces: dict, move: tuple, turn: tuple) -> bool:
	return (check_orthogonal_win(all_pieces, move, turn) 
		 or check_diagonal_win(all_pieces, move, turn))

#	MINIMAX
def	speculate(pieces: dict, turn: tuple, alpha = float('inf'), beta = float('-inf')) -> int:
	pass

def	minimax(pieces: dict, turn: tuple) -> tuple:
	
	pass