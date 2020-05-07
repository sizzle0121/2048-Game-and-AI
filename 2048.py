from agent import Agent
from board import Board
from analyze import Analyzer
#from argparse import ArgumentParser

TRAIN = True
EPISODE = 3000
MILESTONE = 500


if __name__ == "__main__":
	Game = Board()
	AI = Agent()
	analysis = Analyzer()
	if TRAIN == True:
		totalR = 0
		for e in range(EPISODE):
			Game.initialize()
			AI.Episode_begin()
			while True:
				act, r = AI.step(Game)
				if r != -1:
					totalR += r
				if Game.end_game():
					break
				Game.GenRandTile(r)
				if Game.end_game():
					break
			AI.Episode_end()
			analysis.eval(Game)
			if e % MILESTONE == 0:
				print("#Episode: {episode}, score: {score}".format(episode = e, score = totalR))	
				totalR = 0
				analysis.printAnalysis(MILESTONE)
				analysis.reset()
				AI.save_tupleNet()
		AI.save_tupleNet()

	else:
		totalR = 0
		for i in range(1):	
			Game.initialize()
			while True:
				act, r = AI.step(Game)
				if r != -1:
					totalR += r
				if Game.end_game():
					break
				Game.GenRandTile(r)
				if Game.end_game():
					break
		Game.printBoard()
		print("Score: {}".format(totalR))
