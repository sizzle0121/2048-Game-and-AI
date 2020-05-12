# Master the 2048 Game	
### Train an AI to crack the game!		
	
### Live Demo		
Gameplay by AI		
	
	
	
![demo](https://github.com/sizzle0121/2048-Game-and-AI/blob/master/img/demo.gif)		
	
Launch and play the game (human player)		
![demo1](https://github.com/sizzle0121/2048-Game-and-AI/blob/master/img/demo1.gif)			
		



### How to Run?		
* To play the game		
>	`python3 2048.py`		
	
* To see arguments		
>	`python3 2048.py -h`	
	
* To train your AI (the tuple network will be saved to the directory tupleNet/)		
>	`python3 2048.py --play=n --train=on -e=5000 -m=500`		
	
* To test your AI for one game round		
>	`python3 2048.py --play=n --train=off`		
	
	
	
### How to Control?		
* Press arrow keys or w/a/s/d to move the tiles up/left/down/right		
* Press 'h' to get a hint from your AI (let it move the critical step for you)			
* Press 'z' to see how your AI crack the game (lazy mode, auto play by AI)		
* Auto play mode can be toggled by pressing 'z' again		
	
	

### N-Tuple Network		
Use combinations of tiles to extract the features of the game board.	
By updating the state-value of features, the value states of the game board will be the sum of the value of the features. This mapping from combinations of tiles to the state-value is the value function.		
Here, I implement 6644-tuple network.		
![tupleNetwork](https://github.com/sizzle0121/2048-Game-and-AI/blob/master/img/tuple-network.png)		
	
	
		
	
### Temporal Difference Learning			
I implement TD(0) after state learning.			
The "after state" is like the Q(s, a) value.		
![TDL](https://github.com/sizzle0121/2048-Game-and-AI/blob/master/img/TDL.png)			
	
	

	
### Future Development		
>		
>* Add expectimax search to enhance the performance.		
>* Implement BitBoard to speed up training.		
>* Implementing DQN to extract features and train may be interesting as well.		
