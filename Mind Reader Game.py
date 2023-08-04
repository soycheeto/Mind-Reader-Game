import random
import numpy as np
last_1 = 0
last_2 = 0


inputs = np.zeros(shape=(2, 2, 2), dtype=int)
inputs

def update_inputs(current):
  global last_1, last_2
  if inputs[last_2][last_1][0] == current:
    inputs[last_2][last_1][1] = 1 
    inputs[last_2][last_1][0] = current
  else:
    inputs[last_2][last_1][1] = 0 
    inputs[last_2][last_1][0] = current
 
  last_2 = last_1 
  last_1 = current

def prediction():
  if inputs[last_2][last_1][1] == 1: 
    predict = inputs[last_2][last_1][0]    
  else:
    predict = random.randint(0, 1)  
  return predict 

scores = [0,  0] #computer score, player score
def update_scores(predicted, player_input):
  if predicted == player_input:
    scores[0] = scores[0] + 1
    print("Computer score is:", scores[0], "Player score is:", scores[1])
  else:
    scores[1] = scores[1] + 1
    print("Computer score is:", scores[0], "Player score is:", scores[1])
  

def reset():
  for i in range(2):
    for j in range(2):
      for k in range(2):
        inputs[i][j][k] = 0
  
  for i in range(len(scores)):
    scores[i] = 0

def gameplay():
  reset()
  print("Initial inputs array:", inputs)
  print("Initial scores list:", scores)

  valid_entries = ['0', '1']

  while True:
    predicted = prediction()
    player_input = input("Enter either 0 or 1:")
    while player_input not in valid_entries:
      print("Invalid input!")
      player_input = input("Please enter either 0 or 1:")

    player_input = int(player_input)

    update_inputs(player_input)
    update_scores(predicted, player_input)

    if scores[0] == 10:
      print("You lost!")
      break
    elif scores[1] == 10:
      print("You won!")
      break
