from art import logo, vs
from game_data import data
import random
from os import system

def game(score):
  object = random.choice(data)
  x = True
  while(x == True):
    print(f"Compare A: {object['name']}, {object['description']}, from {object['country']}")
    print(vs)
    list = []
    for object2 in data:
      if object2 == data[data.index(object)]:
        continue
      list.append(object2)
        
    object2 = random.choice(list)
    print(f"Against B: {object2['name']}, {object2['description']}, from {object2['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == 'A' and object['follower_count'] > object2['follower_count']:
      score += 1
      system('clear')
      print(logo)
      print(f"You're right! Current score is {score}")
      object = object2
    elif choice == 'B' and object['follower_count'] < object2['follower_count']:
      score += 1
      system('clear')
      print(logo)
      print(f"You're right! Current score is {score}")
      object = object2
    else:
      print(f"You lost. Your score is {score}")
      return

score = 0
print(logo)

game(score)