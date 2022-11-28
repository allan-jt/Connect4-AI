from Utils import *

#	SCORE CALCULATOR
def	calculate_score(board: dict, turn: tuple) -> int:
	# Score can be refined by checking whether the current
	# link can be expanded. Think about this later.

	d_score = diagonal_score(board, turn)
	o_score = orthogonal_score(board, turn)
#	print("Diagonal: ", d_score, " Orthogonal: ", o_score)
	return (d_score + o_score)

def	orthogonal_score(board: dict, cur_turn: tuple) -> int:
	scores = {RED: 0, YELLOW: 0}

	for posY in range(GAME_HEIGHT):
		posX = 0
		while posX < GAME_WIDTH:
			whites, position = traverse(board, WHITE, (posX, posY), HORIZONTAL)
			if position[X] >= GAME_WIDTH:
				break
			turn = board[position]
			counter, position = traverse(board, turn, position, HORIZONTAL)
			
			posX = position[X]
			start_white = (whites > 0)
			end_white = (posX < GAME_WIDTH and board[position] == WHITE)
			winning = (counter >= WIN)
			scores[turn] += (SCORING[counter] * (start_white + end_white + winning))
	
	for posX in range(GAME_WIDTH):
		posY = 0
		while posY < GAME_HEIGHT:
			whites, position = traverse(board, WHITE, (posX, posY), VERTICAL)
			if position[Y] >= GAME_HEIGHT:
				break
			turn = board[position]
			counter, position = traverse(board, turn, position, VERTICAL)
			
			posY = position[Y]
			start_white = (whites > 0)
			end_white = (posY < GAME_HEIGHT and board[position] == WHITE)
			winning = (counter >= WIN)
			scores[turn] += (SCORING[counter] * (start_white + end_white + winning))
	
	return (scores[RED] - scores[YELLOW])

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
		whites, position = traverse(board, WHITE, position, direction)
		if not within_bounds(position[X], position[Y]):
			break
		turn = board[position]
		counter, position = traverse(board, turn, position, direction)
		
		start_white = (whites > 0)
		end_white = (within_bounds(position[X], position[Y]) and board[position] == WHITE)
		winning = (counter >= WIN)
		scores[turn] += (SCORING[counter] * (start_white + end_white + winning))

	return (scores[RED] - scores[YELLOW]) 

def	traverse(board: dict, turn: tuple, position: tuple, direction: tuple):
	counter = 0
	while same_color(board, position, turn):
		counter += 1
		position = increment(position, direction[X], direction[Y])
	return counter, position
