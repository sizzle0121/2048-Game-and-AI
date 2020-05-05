import numpy as np
import random
import copy

class Board():
	def __init__(self):
		self.tile = np.zeros((4, 4), dtype = np.uint32)

	def initialize(self):
		pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
		random.shuffle(pos)
		for i in range(2):
			x = pos[i] // 4
			y = pos[i] % 4
			num = random.randint(1, 101)
			if num <= 75:
				self.tile[x][y] = 1
			else:
				self.tile[x][y] = 2
	

	def GenRandTile(self):
		x, y = -1, -1
		while True:
			pos = random.randint(0, 15)
			if self.tile[pos // 4][pos % 4] == 0:
				x = pos // 4
				y = pos % 4
				break
		num = random.randint(1, 101)
		if num <= 75:
			self.tile[x][y] = 1
		else:
			self.tile[x][y] = 2


	def copyBoard(self, tmp):
		self.tile = tmp.copy()	

	def move(self, op):
		if op == 0:
			return self.move_up()
		elif op == 1:
			return self.move_right()
		elif op == 2:
			return self.move_down()
		elif op == 3:
			return self.move_left()
		else:
			return -1


	def move_left(self):
		prev = self.tile.copy()
		score = 0
		for row in self.tile:
			top = 0
			hold = 0
			for i, num in enumerate(row):
				if num == 0:
					continue
				row[i] = 0
				if hold:
					if num == hold:
						row[top] = num + 1
						top += 1
						score += (np.uint32(1) << (num+1))
						hold = 0
					else:
						row[top] = hold
						top += 1
						hold = num
				else:
					hold = num
			if hold:
				row[top] = hold
		
		if np.array_equal(prev, self.tile):
			return -1
		else:
			return score

	def move_right(self):
		self.reflect_horizontal()
		score = self.move_left()
		self.reflect_horizontal()
		return score

	def move_up(self):
		self.rotate_right()
		score = self.move_right()
		self.rotate_left()
		return score

	def move_down(self):
		self.rotate_right()
		score = self.move_left()
		self.rotate_left()
		return score

	def transpose(self):
		self.tile = self.tile.transpose()

	def reflect_horizontal(self):
		self.tile = np.fliplr(self.tile)
	
	def reflect_vertical(self):
		self.tile = np.flipud(self.tile)

	def rotate_right(self):
		self.tile = np.rot90(self.tile, 1, (1, 0))
	
	def rotate_left(self):
		self.tile = np.rot90(self.tile)

	def reverse(self):
		self.reflect_horizontal()
		self.reflect_vertical()


	def printBoard(self):
		print(self.tile)






if __name__ == "__main__":
	b = Board()
	b.initialize()
	b.printBoard()
	print()
	b.rotate_right()
	b.printBoard()
	b.rotate_left()
	b.printBoard()
	print()
	b.GenRandTile()
	b.move_right()
	b.printBoard()
	print()
	b.GenRandTile()
	b.move_up()
	b.printBoard()
	print()
	b.GenRandTile()
	b.move_down()
	b.printBoard()
