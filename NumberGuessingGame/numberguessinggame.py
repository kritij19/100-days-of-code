import random
#from replit import clear
from art import logo, vs
from game_data import data

def winner(A_follower_count, B_follower_count):
  '''Decides the winner by comparing follower counts'''
  if A_follower_count > B_follower_count:
    return 'A'
  else:
    return 'B'


game_continue = True
score = 0
while game_continue:
  #clear()
  print(logo)

  # Randomly choose first two options
  if score == 0:
    A = random.choice(data)
    B = random.choice(data)
  # Display score after correct guess
  else:
    print(f"You're right! Current score: {score}") 
  
  A_count = A['follower_count']
  B_count = B['follower_count']
  

  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
  print(f"{vs}\n")
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

  guess = input("\nWho has more followers? Type 'A' or 'B': ")
  # If the user makes a correct guess Option B now becomes option A and a random option B is chosen
  if guess == winner(A_count, B_count):
    A = B
    B = random.choice(data)

    score += 1
  else:
    game_continue = False
    #clear()
    print(f"Your guess is wrong. Your final score is {score}")
