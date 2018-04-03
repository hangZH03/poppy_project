from PIL import Image, ImageDraw, ImageFont
import numpy as np

img = Image.new( 'RGB', (600,700), "white")
pixels = img.load() # create the pixel map

fnt = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 15)
d = ImageDraw.Draw(img)
d.text((150,650), "Reiniciar", font=fnt, fill=(0, 0, 0))
d.text((300,650), "Puntajes", font=fnt, fill=(0, 0, 0))
d.text((450,650), "Jugar", font=fnt, fill=(0, 0, 0))

black = (0,0,0)
yellow = (255,221,0)
blue = (3,78,162)

board_x_lim = 600
board_y_lim = 600
line_tickness = 6

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


board = [['x', 'o', 'x'], [' ', ' ', ' '], [' ', ' ', ' ']]

for x in range(0,3):
	print board[x]

empty = ' '
player_1 = 'x'
player_2 = 'o'

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

img.show()