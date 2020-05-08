from gamegrid import GameGrid
from argparse import ArgumentParser
from trainer import Trainer


parser = ArgumentParser()
parser.add_argument("--play", help = "Play the game or not (y/n), default: y", dest="play", default="y")
parser.add_argument("--train", help = "Train mode (on/off), default: off", dest="train", default="off")
parser.add_argument("-e", help = "Total episodes to train (recommend less than 10000 per time), default: 1000", dest="episode", type=int, default=1000)
parser.add_argument("-m", help = "Set milestone to save tuple nets and show the training statistics, default: 500", dest="milestone", type=int, default=500)

args = parser.parse_args()



if __name__ == "__main__":
	if args.play == "n":
		PLAY = False
	else:
		PLAY = True
	if args.train == 'on':
		TRAIN = True
	else:
		TRAIN = False
	EPISODE = args.episode
	MILESTONE = args.milestone
	

	if PLAY:
		print("\n\n")
		print("#########		Use Arrow Keys or w/a/s/d to move tiles UP/LEFT/DOWN/RIGHT")
		print("#########		Wanna get a hint?") 
		print("#########		Press 'h' to let the AI to help moving the critical step for you!")
		print("#########		Can't breakthrough your personal record?") 
		print("#########		Press 'z' to see how the AI crack this game! (AI auto play mode)")
		print("")
		print("auto play mode can be toggled by pressing 'z' again\n\n")
		Game2048 = GameGrid()

	else:
		trainer = Trainer(TRAIN, EPISODE, MILESTONE)

