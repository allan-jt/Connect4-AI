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
			start_whites, position = traverse(board, WHITE, (posX, posY), HORIZONTAL)
			if position[X] >= GAME_WIDTH:
				break
			
			turn = board[position]
			counter, position = traverse(board, turn, position, HORIZONTAL)
			posX = position[X]

			end_whites, position = traverse(board, WHITE, position, HORIZONTAL)
			scores[turn] += get_score(counter, start_whites, end_whites)
	
	for posX in range(GAME_WIDTH):
		posY = 0
		while posY < GAME_HEIGHT:
			start_whites, position = traverse(board, WHITE, (posX, posY), VERTICAL)
			if position[Y] >= GAME_HEIGHT:
				break
			
			turn = board[position]
			counter, position = traverse(board, turn, position, VERTICAL)
			posY = position[Y]

			end_whites, position = traverse(board, WHITE, position, VERTICAL)
			scores[turn] += get_score(counter, start_whites, end_whites)
	
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
		start_whites, position = traverse(board, WHITE, position, direction)
		if not within_bounds(position[X], position[Y]):
			break
		
		turn = board[position]
		counter, position = traverse(board, turn, position, direction)
		
		end_whites, tmp_position = traverse(board, WHITE, position, direction)
		scores[turn] += get_score(counter, start_whites, end_whites)

	return (scores[RED] - scores[YELLOW]) 

def	traverse(board: dict, turn: tuple, position: tuple, direction: tuple):
	counter = 0
	while same_color(board, position, turn):
		counter += 1
		position = increment(position, direction[X], direction[Y])
	return counter, position

def	get_score(counter: int, start_whites: int, end_whites: int):
	potential_start = (counter + start_whites) >= WIN
	potential_end = (counter + end_whites) >= WIN
	potential_mid = 0
	if (counter + start_whites + end_whites) >= WIN and (start_whites * end_whites):
		potential_mid = 1

	return SCORING[counter] * (potential_start + potential_end + potential_mid)