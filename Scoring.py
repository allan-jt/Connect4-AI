from Utils import *

def	calculate_score(board: dict, turn: tuple) -> int:
	return diagonal_score(board, turn) + orthogonal_score(board, turn)

# 	ORTHOGONAL
def	orthogonal_score(board: dict, cur_turn: tuple) -> int:
	scores = {RED: 0, YELLOW: 0}

	for posY in range(GAME_HEIGHT):
		posX = 0
		while posX < GAME_WIDTH:
			start_spaces, position = traverse(board, WHITE, (posX, posY), HORIZONTAL)
			if position[X] >= GAME_WIDTH:
				break
			
			turn = board[position]
			counter, position = traverse(board, turn, position, HORIZONTAL)
			posX = position[X]

			end_spaces, position = traverse(board, WHITE, position, HORIZONTAL)
			scores[turn] += get_score(counter, start_spaces, end_spaces)
	
	for posX in range(GAME_WIDTH):
		posY = 0
		while posY < GAME_HEIGHT:
			start_spaces, position = traverse(board, WHITE, (posX, posY), VERTICAL)
			if position[Y] >= GAME_HEIGHT:
				break
			
			turn = board[position]
			counter, position = traverse(board, turn, position, VERTICAL)
			posY = position[Y]

			end_spaces, position = traverse(board, WHITE, position, VERTICAL)
			scores[turn] += get_score(counter, start_spaces, end_spaces)
	
	return (scores[RED] - scores[YELLOW])

#	DIAGONAL
def	diagonal_score(board: type, cur_turn: tuple) -> int:
	score = 0

	for height in range(GAME_HEIGHT):
		score += get_diagonal_score(board, DIAGONAL_UP, (0, height), cur_turn)
		score += get_diagonal_score(board, DIAGONAL_DOWN, (0, height), cur_turn)
	
	for width in range(1, GAME_WIDTH):
		score += get_diagonal_score(board, DIAGONAL_UP, (width, GAME_HEIGHT - 1), cur_turn)
		score += get_diagonal_score(board, DIAGONAL_DOWN, (width, 0), cur_turn)
		
	return score

def get_diagonal_score(board: type, direction: tuple, position: tuple, cur_turn: tuple):
	scores = {RED: 0, YELLOW: 0}

	while within_bounds(position[X], position[Y]):
		start_spaces, position = traverse(board, WHITE, position, direction)
		if not within_bounds(position[X], position[Y]):
			break
		
		turn = board[position]
		counter, position = traverse(board, turn, position, direction)
		
		end_spaces, tmp_position = traverse(board, WHITE, position, direction)
		scores[turn] += get_score(counter, start_spaces, end_spaces)

	return (scores[RED] - scores[YELLOW]) 

#	UTILITIES
def	traverse(board: dict, turn: tuple, position: tuple, direction: tuple):
	counter = 0
	while same_color(board, position, turn):
		counter += 1
		position = increment(position, direction[X], direction[Y])
	return counter, position

def	get_score(counter: int, start_spaces: int, end_spaces: int):
	potential_start = (counter + start_spaces) >= WIN
	potential_end = (counter + end_spaces) >= WIN
	potential_mid = 0
	if (counter + start_spaces + end_spaces) >= WIN and (start_spaces * end_spaces):
		potential_mid = 1

	return SCORING[counter] * (potential_start + potential_end + potential_mid)