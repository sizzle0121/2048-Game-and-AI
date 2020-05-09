from board import Board
import numpy as np
import random
import os


class Agent():
	def __init__(self):
		self.episode = []
		self.net = []
		self.alpha = 0.0025
		self.gamma = 1.0
		if os.path.isfile("tupleNet/tuple1.npy"):
			print("Found tuple network")
			print("Loading...")
			self.load_tupleNet("tupleNet/tuple")
		else:
			print("Building tuple Network...")
			self.build_tupleNet()
			print("Completed")


	def build_tupleNet(self):
		self.net.append(np.zeros(shape=(20, 20, 20, 20, 20, 20), dtype=np.float32))
		self.net.append(np.zeros(shape=(20, 20, 20, 20, 20, 20), dtype=np.float32))
		self.net.append(np.zeros(shape=(20, 20, 20, 20), dtype=np.float32))
		self.net.append(np.zeros(shape=(20, 20, 20, 20), dtype=np.float32))
		
	def load_tupleNet(self, filename):
		for i in range(4):
			self.net.append(np.load(filename+str(i+1)+".npy"))

	def save_tupleNet(self):
		for i in range(4):
			np.save("tupleNet/tuple%d" % (i+1), self.net[i])

	def updateNet(self, tmp, TD_error):
			self.net[0][tmp.getTile(0)][tmp.getTile(4)][tmp.getTile(8)][tmp.getTile(1)][tmp.getTile(5)][tmp.getTile(9)] += TD_error
			self.net[1][tmp.getTile(1)][tmp.getTile(5)][tmp.getTile(9)][tmp.getTile(2)][tmp.getTile(6)][tmp.getTile(10)] += TD_error
			self.net[2][tmp.getTile(2)][tmp.getTile(6)][tmp.getTile(10)][tmp.getTile(14)] += TD_error
			self.net[3][tmp.getTile(3)][tmp.getTile(7)][tmp.getTile(11)][tmp.getTile(15)] += TD_error
		

	def getV(self, b):
		v = 0.0
		tmp = Board()
		for i in range(8):
			tmp.copyBoard(b)
			tmp.morphBoard(i)
			v += self.net[0][tmp.getTile(0)][tmp.getTile(4)][tmp.getTile(8)][tmp.getTile(1)][tmp.getTile(5)][tmp.getTile(9)]
			v += self.net[1][tmp.getTile(1)][tmp.getTile(5)][tmp.getTile(9)][tmp.getTile(2)][tmp.getTile(6)][tmp.getTile(10)]
			v += self.net[2][tmp.getTile(2)][tmp.getTile(6)][tmp.getTile(10)][tmp.getTile(14)]
			v += self.net[3][tmp.getTile(3)][tmp.getTile(7)][tmp.getTile(11)][tmp.getTile(15)]
		return v




	def Episode_begin(self):
		self.episode = []
		
	def Episode_end(self):
		last = True
		while len(self.episode) > 0:
			a = self.episode[-1]['after']
			b = self.episode[-1]['before']
			R = self.episode[-1]['reward']
			S_, S = self.getV(a), self.getV(b)
			tmp = Board()
			for i in range(8):
				tmp.copyBoard(b)
				tmp.morphBoard(i)
				if last == False:
					self.updateNet(tmp, self.alpha*(R + S_ - S))
				else:
					self.updateNet(tmp, self.alpha*(0 - S))
			last = False
			del self.episode[-1]

		
	def step(self, prev):		
		#action = random.randint(0, 3)
		#reward = prev.move(action)
		#return action, reward
		
		maxV = float(-1e9)
		maxOP = -1
		tmp = Board()
		for op in range(4):
			tmp.copyBoard(prev)
			r = tmp.move(op)
			if r != -1:
				v = self.getV(tmp)
				if v+r >= maxV:
					maxV = v+r
					maxOP = op
		
		if maxOP != -1:
			r = prev.move(maxOP)
			tmp.copyBoard(prev)
			state = {
			'before': tmp,
			'after': tmp,
			'reward': r,
			'action': maxOP
			}
			if len(self.episode) > 0:
				self.episode[-1]['after'] = tmp
			self.episode.append(state)
			return maxOP, r
		else:
			return -1, -1
		


if __name__ == "__main__":
	AI = Agent()
	EPISODE = 1001
	for e in range(EPISODE):
		B = Board()
		B.initialize()
		while True:
			act, r = AI.step(B)
			if B.end_game():
				break
			B.GenRandTile(r)
			if B.end_game():
				break
			#B.printBoard()
		if e % 100 == 0:
			print("#Episode: {episode}".format(episode = e))
			B.printBoard()
