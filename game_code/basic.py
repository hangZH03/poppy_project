import time
from random import randint

w, h = 3, 3
empty = ' '
player_1 = 'X'
player_2 = 'O'
poppy = player_2
board = [[empty for x in range(w)] for y in range(h)]
n_play = 0
current_player = player_1
current_winner = empty


def print_board():
	print "========="
	for ptr in range (w):
		print board[ptr]
	print "========="

def play(row,col):
	global board
	global n_play
	global current_player
	global current_winner
	global poppy
	global empty
	if(current_winner == empty):
		if(board [row][col] == empty):
			n_play = n_play+1
			board [row][col] = current_player
			if(check_win()):
				print "Winner: " + str(current_player) + ", reset the game"
				current_winner = current_player
			else:
				if(n_play < 9):
					if(current_player == player_1):
						current_player = player_2
					else:
						current_player = player_1
				else:
					print "Tie, reset the game"
					current_winner = 'None'
			print_board()
		else:
			if(current_player != poppy):
				print  "Already taken! Try again"
	else:
		print "Winner: " + str(current_player) + ", reset the game"

def validate_poppy_move(row,col):
	global board
	global empty
	if(board [row][col] == empty):
		return True
	else:
		return False

def check_win():
	global current_player
	isWin = False
	for row in range(h):
		if(board[row][0] == current_player and board[row][1] == current_player and board[row][2] == current_player):
			isWin = True
	for col in range(w):
		if(board[0][col] == current_player and board[1][col] == current_player and board[2][col] == current_player):
			isWin = True
	if(board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player):
		isWin = True
	if(board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player):
		isWin = True
	return isWin

def set_poppy_player():
	n_player_for_poppy = raw_input("Player Number for Poppy (1 or 2): << ")
	while(int(n_player_for_poppy) != 1 and int(n_player_for_poppy) != 2):
		n_player_for_poppy = raw_input("Incorrect number, try again (1 or 2): << ")
	return int(n_player_for_poppy)

def reset():
	global current_player
	global current_winner
	global board
	global n_play
	global poppy
	current_player = player_1
	current_winner = empty
	if(set_poppy_player() == 1):
		poppy = player_1
	else:
		poppy = player_2
	board = [[empty for x in range(w)] for y in range(h)]
	n_play = 0
	print "Start!"
	print_board()


reset()

while(current_winner == empty):
	if(current_player == poppy):
		print("Poppy's Turn...")
		isValid = False
		while(not(isValid)):
			row = randint(0,2)
			col = randint(0,2)
			isValid = validate_poppy_move(row,col)
		print ("Poppy's moving his hand...")
		time.sleep(0.5)
	else:
		print("Your Turn...")
		row = raw_input("Row: << ")
		col = raw_input("Col: << ")
		while(int(row) > 2 or int(row) < 0 or int(col) > 2 or int(col) < 0):
			print "Out of range, re-enter values"
			row = raw_input("Row: << ")
			col = raw_input("Col: << ")

	play(int(row),int(col))