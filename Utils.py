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


#	SCORE CALCULATOR
def	calculate_score(board: tuple) -> int:
	# Score can be refined by checking whether the current
	# link can be expanded. Think about this later.
	d_score = diagonal_score(board)
	o_score = orthogonal_score(board)
#	print("Diagonal: ", d_score, " Orthogonal: ", o_score)
	return (d_score + o_score)

def	orthogonal_score(board: type) -> int:
	scores = {RED: 0, YELLOW: 0}
	
	turn = RED	# score horizontal
	for height in range(GAME_HEIGHT):	
		counter = 0
		for width in range(GAME_WIDTH):
			if board[(width, height)] != turn:
				scores[turn] += SCORING[counter]
				turn = swap_color(turn)
				counter = 0
			counter += (board[(width, height)] == turn)
		scores[turn] += SCORING[counter]

	turn = RED	# score vertical
	for width in range(GAME_WIDTH):	
		counter = 0
		for height in range(GAME_HEIGHT):
			if board[(width, height)] != turn:
				scores[turn] += SCORING[counter]
				turn = swap_color(turn)
				counter = 0
			counter += (board[(width, height)] == turn)
		scores[turn] += SCORING[counter]

	return (scores[RED] - scores[YELLOW])
 
def	diagonal_score(board: type) -> int:
	score = 0
	up = True		# Upward scoring
	down = False	# downward scoring

	for height in range(GAME_HEIGHT):
		score += get_diagonal_score(board, up, (0, height))
		score += get_diagonal_score(board, down, (0, height))
	
	for width in range(1, GAME_WIDTH):
		score += get_diagonal_score(board, up, (width, GAME_HEIGHT - 1))
		score += get_diagonal_score(board, down, (width, 0))
		
	return score
	
def	get_diagonal_score(board: type, direction_up: bool, position: tuple):
	scores = {RED: 0, YELLOW: 0}
	posX = position[X]
	posY = position[Y]
	counter = 0
	turn = RED
	i = 1 if direction_up else -1

	while within_bounds(posX := posX - 1, posY := posY + i):
		continue
	while within_bounds(posX := posX + 1, posY := posY - i):
		if board[(posX, posY)] != turn:
			scores[turn] += SCORING[counter]
			turn = swap_color(turn)
			counter = 0
		counter += (board[(posX, posY)] == turn)
	scores[turn] += SCORING[counter]
	return (scores[RED] - scores[YELLOW])


#	OTHER UTILITIES
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

def	get_free_spaces(board: dict, turn: tuple) -> list:
	free_spaces: list = []	# all free spaces
	for width in range(GAME_WIDTH):
		for height in range(GAME_HEIGHT - 1, -1, -1):
			if board[(width, height)] == WHITE:
				free_spaces.append((width, height))
				break
	
	win_lose_spaces: list = []	# win/lose spaces
	enemy_turn = swap_color(turn)
	for space in free_spaces:
		board[space] = turn
		if check_win(board, space, turn):
			win_lose_spaces.append(space)
			board[space] = WHITE
			continue
		board[space] = enemy_turn
		if check_win(board, space, enemy_turn):
			win_lose_spaces.append(space)
		board[space] = WHITE

	if len(win_lose_spaces) > 0:
		return win_lose_spaces
	return free_spaces

def	within_bounds(positionX: int, positionY: int) -> bool:
	return (0 <= positionX < GAME_WIDTH 
		and 0 <= positionY < GAME_HEIGHT)

def	same_color(board: dict, position: tuple, color: tuple) -> bool:
	return (within_bounds(position[X], position[Y])
		and board[position] == color)