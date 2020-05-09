from board import Board
import numpy as np

class Analyzer():
	def __init__(self):
		self.nums = {}
		self.top = int(0)
		self.reset()

	def eval(self, b):
		tiles = b.getBoard()
		for row in tiles:
			for c in row:
				if c != 0:
					self.nums[str(c)] += 1
					if c > self.top:
						self.top = c

	def printAnalysis(self, milestone):
		for i in range(self.top, self.top-5, -1):
			print("{}: {:.2%}".format((np.int32(1) << np.int32(i)), (self.nums[str(i)] / milestone)))


	def reset(self):
		self.top = int(0)
		self.nums = {
		'1': 0,
		'2': 0,
		'3': 0,
		'4': 0,
		'5': 0,
		'6': 0,
		'7': 0,
		'8': 0,
		'9': 0,
		'10': 0,
		'11': 0,
		'12': 0,
		'13': 0,
		'14': 0,
		'15': 0,
		'16': 0,
		'17': 0,
		'18': 0,
		'19': 0,
		'20': 0
		}
