from Constants import *
import random

#	UTILS
def swapColor(color: tuple) -> tuple:
	if color == YELLOW:
		return RED
	if color == RED:
		return YELLOW
	return color

def	is_space_left(all_pieces: dict) -> bool:
	for piece in all_pieces.values():
		if piece.color == WHITE:
			return True
	return False

def	is_within_bounds(positionX: int, positionY: int) -> bool:
	return (positionX < GAME_WIDTH and positionY < GAME_HEIGHT
		and positionX >= 0 and positionY >= 0)

def check_orthogonal_win(all_pieces: dict, move: tuple, turn: tuple) -> bool:
	counter = 0	# check horizontal
	for width in range(GAME_WIDTH):
		if all_pieces[(width, move[Y])].color != turn:
			counter = 0
		elif (counter := counter + 1) == 4:
			return True

	counter = 0 # check vertical
	for height in range(GAME_HEIGHT):
		if all_pieces[(move[X], height)].color != turn:
			counter = 0
		elif (counter := counter + 1) == 4:
			return True

	return False

#	VALIDATE WIN
def	check_diagonal_win(all_pieces: dict, move: tuple, turn: tuple) -> bool:
	counter = 1	# check / diagonal
	posX = move[X]
	posY = move[Y]
	while is_within_bounds(posX := posX + 1, posY := posY + 1):
		if all_pieces[(posX, posY)].color != turn:
			break
		counter += 1
	posX = move[X]
	posY = move[Y]
	while is_within_bounds(posX := posX - 1, posY := posY - 1):
		if all_pieces[(posX, posY)].color != turn:
			break
		counter += 1
	if counter == WIN:
		return True

	counter = 1	# check \ diagonal
	posX = move[X]
	posY = move[Y]
	while is_within_bounds(posX := posX + 1, posY := posY - 1):
		if all_pieces[(posX, posY)].color != turn:
			break
		counter += 1
	posX = move[X]
	posY = move[Y]
	while is_within_bounds(posX := posX - 1, posY := posY + 1):
		if all_pieces[(posX, posY)].color != turn:
			break
		counter += 1
	if counter == WIN:
		return True

	return False


def	check_win(all_pieces: dict, move: tuple, turn: tuple) -> bool:
	return (check_orthogonal_win(all_pieces, move, turn) 
		 or check_diagonal_win(all_pieces, move, turn))

#	MINIMAX
def	speculate(all_pieces: dict, turn: tuple, alpha = float('inf'), beta = float('-inf')) -> int:
	pass

def	minimax(all_pieces: dict, turn: tuple) -> tuple:
	
	pass