from art import *
import random
from game_data import data
from replit import clear

Condition = True
points = 0


#Ignoring the follower_count key
def key_seperate(x):
  ignore_key = ('follower_count')
  filtered_dict = {k: v for k, v in x.items() if k not in ignore_key}
  global list1
  list1 = list(filtered_dict.values())


def check_answer():
  global Condition
  global points
  if A > B:
    if guess_ans == "A":
      points += 1
    else:
      print(f"Sorry, that's wrong. Final score: {points}")
      Condition = False
  elif B > A:
    if guess_ans == "B":
      points += 1
    else:
      print(f"Sorry, that's wrong. Final score: {points}")
      Condition = False


while Condition:
  print(logo)
  que1 = random.choice(data)
  data.remove(que1)
  que2 = random.choice(data)
  data.remove(que2)
  key_seperate(x=que1)
  print("Compare A:", end=" ")
  print(*list1, sep=', ')
  print(vs)
  key_seperate(x=que2)
  print("Against B:", end=" ")
  print(*list1, sep=', ')
  guess_ans = input("Who has more followers? Type 'A' or 'B': ")
  A = que1['follower_count']
  B = que2['follower_count']
  clear()
  check_answer()

  while Condition:
    print(logo)
    print(f"You're right! current score: {points}")
    que3 = random.choice(data)
    key_seperate(x=que2)
    print("Compare A:", end=" ")
    print(*list1, sep=', ')
    print(vs)
    key_seperate(x=que3)
    print("Against B:", end=" ")
    print(*list1, sep=', ')
    A = que2['follower_count']
    B = que3['follower_count']
    guess_ans = input("Who has more followers? Type 'A' or 'B': ")
    clear()
    check_answer()
    que2 = que3
    data.remove(que3)
