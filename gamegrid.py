from tkinter import Frame, Label, CENTER
import numpy as np
from board import Board
from agent import Agent
import constants as c
import time

class GameGrid(Frame):
	def __init__(self):
		Frame.__init__(self)
		
		self.grid()
		self.master.title('2048 designed by Sizzle')
		self.master.bind("<Key>", self.key_press)

		self.Game = Board()
		self.AI = Agent()
		self.matrix = np.zeros((4,4))
		self.grid_cells = []
		self.init_grid()
		self.matrix = self.Game.getBoard()
		self.update_grid_cells()
				
		self.commands = {c.KEY_UP_ALT: 0, c.KEY_RIGHT_ALT: 1, c.KEY_DOWN_ALT: 2,
			c.KEY_LEFT_ALT: 3, c.KEY_UP: 0, c.KEY_RIGHT: 1, c.KEY_DOWN: 2,
			c.KEY_LEFT: 3
		}
		self.score = 0
		self.dir = ["Up", "Right", "Down", "Left"]
		self.AUTOPLAY = False
		self.HINT = False
		while True:		
			while self.AUTOPLAY or self.HINT:
				act, r = self.AI.step(self.Game)
				if r != -1:
					self.score += r
				if self.Game.end_game():
					break
				self.Game.GenRandTile(r)
				if self.Game.end_game():
					break
				self.matrix = self.Game.getBoard()
				self.update_grid_cells()
				print("\nMove {}".format(self.dir[act]))
				print("Current Score: {}".format(self.score))
				self.HINT = False
				time.sleep(1)
			self.update_grid_cells()
			self.update()
		self.mainloop()

	def init_grid(self):
		background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
						   width=c.SIZE, height=c.SIZE)
		background.grid()

		for i in range(c.GRID_LEN):
			grid_row = []
			for j in range(c.GRID_LEN):
				cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
							 width=c.SIZE / c.GRID_LEN,
							 height=c.SIZE / c.GRID_LEN)
				cell.grid(row=i, column=j, padx=c.GRID_PADDING,
						  pady=c.GRID_PADDING)
				cell.grid_propagate(False)
				t = Label(master=cell, text="",
						  bg=c.BACKGROUND_COLOR_CELL_EMPTY,
						  justify=CENTER, font=c.FONT, width=5, height=3)
				t.grid()
				grid_row.append(t)

			self.grid_cells.append(grid_row)


	def update_grid_cells(self):
		for i in range(c.GRID_LEN):
			for j in range(c.GRID_LEN):
				new_number = (np.uint32(1) << np.int32(self.matrix[i][j]))
				if new_number == 1:
					self.grid_cells[i][j].configure(
						text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
				else:
					self.grid_cells[i][j].configure(text=str(
						new_number), bg=c.BACKGROUND_COLOR_DICT[new_number],
						fg=c.CELL_COLOR_DICT[new_number])
		self.update_idletasks()
		self.update()
		

	def key_press(self, event):
		key = repr(event.char)
		act = -1
		if self.AUTOPLAY == False and key == c.KEY_HINT:
			self.HINT = True
		elif self.AUTOPLAY == False and key in self.commands:
			act = self.commands[repr(event.char)]
			r = self.Game.move(act)
			if r != -1:
				self.score += r
			self.Game.GenRandTile(r)
			self.matrix = self.Game.getBoard()
			self.update_grid_cells()
			print("Move {}".format(self.dir[act]))
			print("Current Score: {}".format(self.score))
		elif key == c.KEY_AUTOPLAY:
			if self.AUTOPLAY == False:
				self.AUTOPLAY = True
			else:
				self.AUTOPLAY = False
			
if __name__ == "__main__":
	gamegrid = GameGrid()

