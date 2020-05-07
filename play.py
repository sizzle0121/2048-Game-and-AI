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
		self.master.title('2048')

		self.Game = Board()
		self.Game.initialize()
		self.AI = Agent()
		self.matrix = np.zeros((4,4))
		self.grid_cells = []
		self.init_grid()
		self.score = 0
		self.dir = ["Up", "Right", "Down", "Left"]
		while True:
			self.matrix = self.Game.getBoard()
			self.update_grid_cells()
			act, r = self.AI.step(self.Game)
			if r != -1:
				self.score += r
			if self.Game.end_game():
				break
			self.Game.GenRandTile(r)
			if self.Game.end_game():
				break
			time.sleep(1)
			self.update_idletasks()
			self.update()
			print("Move {}".format(self.dir[act]))
			print("Current Score: {}".format(self.score))
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
				t = Label(master=cell, text="",
						  bg=c.BACKGROUND_COLOR_CELL_EMPTY,
						  justify=CENTER, font=c.FONT, width=5, height=2)
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
		#self.update_idletasks()


if __name__ == "__main__":
	gamegrid = GameGrid()

