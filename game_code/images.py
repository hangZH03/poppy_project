from PIL import Image, ImageDraw, ImageFont
import time
import screeninfo
import sys
import pygame
import numpy as np
from random import randint

# ===== Board constrains =====

w, h = 3, 3
empty = ' '
player_1 = 'X'
player_2 = 'O'
poppy = player_2
board = [[empty for x in range(w)] for y in range(h)]
n_play = 0
current_player = player_1
current_winner = empty

# ===== Image constrains =====

img = Image.new( 'RGB', (600,700), "white")
pixels = img.load() # create the pixel map
black = (0,0,0)
yellow = (255,221,0)
blue = (3,78,162)
board_x_lim = 600
board_y_lim = 600
line_tickness = 6

def play(row,col,board,n_play,current_player,current_winner,poppy,empty):
    if(current_winner == empty):
        if(board [row][col] == empty):
            n_play = n_play+1
            board [row][col] = current_player
            if(check_win(current_player, board)):
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

def validate_poppy_move(row,col,board,empty):
    if(board [row][col] == empty):
        return True
    else:
        return False

def check_win(current_player, board):
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

def set_poppy_player(player_1,player_2):
    global poppy
    n_player_for_poppy = 2 #hardcoded
    if(n_player_for_poppy == 1):
        poppy = player_1
    else:
        poppy = player_2

    return int(n_player_for_poppy)

def reset(player_1,player_2,empty):
    global current_player, current_winner, , board, n_play
    current_player = player_1
    current_winner = empty
    board = [[empty for x in range(w)] for y in range(h)]
    n_play = 0
    print "Start!"

def init_board(img, pixels):
    global black, yellow, blue, board_x_lim, board_y_lim, line_tickness
    fnt = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 15)
    d = ImageDraw.Draw(img)
    d.text((150,650), "Reiniciar", font=fnt, fill=(0, 0, 0))
    d.text((300,650), "Puntajes", font=fnt, fill=(0, 0, 0))
    d.text((450,650), "Jugar", font=fnt, fill=(0, 0, 0))
    for x in range(board_x_lim):
        for y in range(board_y_lim):
            if (x>=0 and x<=line_tickness/2) or (x>=board_x_lim-line_tickness/2 and x<=board_x_lim):
                pixels[x,y] = black
            elif (y>=0 and y<=line_tickness/2) or (y>=board_x_lim-line_tickness/2 and y<=board_x_lim):
                pixels[x,y] = black
            elif (x>=board_x_lim/3-line_tickness/2) and x<=board_x_lim/3+line_tickness/2:
                pixels[x,y] = black
            elif (x>=board_x_lim*2/3-line_tickness/2) and x<=board_x_lim*2/3+line_tickness/2:
                pixels[x,y] = black
            elif (y>=board_y_lim/3-line_tickness/2) and y<=board_y_lim/3+line_tickness/2:
                pixels[x,y] = black
            elif (y>=board_y_lim*2/3-line_tickness/2) and y<=board_y_lim*2/3+line_tickness/2:
                pixels[x,y] = black
    img.save("board.png")
    return

def draw_board(pixels, board):
    global black, yellow, blue, board_x_lim, board_y_lim, line_tickness
    for i in range(0,3):
        for j in range(0,3):
            square_x = np.arange((line_tickness/2+1)+board_x_lim/3*j,(board_x_lim/3-line_tickness/2)+board_x_lim/3*j)
            square_y = np.arange((line_tickness/2+1)+board_y_lim/3*i,(board_y_lim/3-line_tickness/2)+board_y_lim/3*i)
            if(board[i][j] == player_1):
                for x in square_x:
                    for y in square_y:
                        pixels[x,y] = yellow
            elif(board[i][j] == player_2):
                for x in square_x:
                    for y in square_y:
                        pixels[x,y] = blue
    img.save("board.png")
    return

pygame.init()

screen_id = 0
screen = screeninfo.get_monitors()[screen_id]
WIDTH, HEIGHT = screen.width, screen.height

windowSurface = pygame.display.set_mode((0,0), pygame.FULLSCREEN, 32)

gameExit = True
while gameExit:
    events = pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameExit = False
            if event.key == pygame.K_q:
                draw_board(pixels,board)
                windowSurface.blit(pygame.image.load("board.png"), (450, 50))
                pygame.display.flip()
            if event.key == pygame.K_SPACE:
                n_play = reset(empty,player_1,player_2)
                init_board(img, pixels)
                windowSurface.blit(pygame.image.load("board.png"), (450, 50))
                pygame.display.flip()

pygame.quit()
sys.exit()