from art import logo
#from replit import clear
import random



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



# Deals the first two cards to the user and the computer


def computer_plays():
  '''Plays for the computer
  Randomly chooses cards until the sum is less than 17
  After that it randomly chooses whether to pick a card or not.'''
  while sum(computer_hand) < 17:
    computer_hand.append(random.choice(cards))
  if sum(computer_hand) < 22:
    pick_card = [0, 1]
    next_move = random.choice(pick_card)
    if next_move == 0:
      computer_hand.append(random.choice(cards))
      # Replaces 11 with 1 if sum is going over 21
      if 11 in computer_hand and sum(computer_hand) > 21: 
          computer_hand.remove(11)
          computer_hand.append(1)



def game_over(u_score, c_score):
  '''Checks if either tha computer or the user has gone bust or has a blackjack.'''
  if c_score == 21:
    print(f"""\nThe computer has a blackjack, Computer's final hand: {computer_hand}
YOU LOSE :(""")
    return True
  elif u_score == 21:
    print("\nYou have a blackjack, YOU WIN!")
    return True
  elif u_score > 21:
    print(f"""\nYou went over, YOU LOSE :(""")
    return True
  elif c_score >21:
    print(f"""\nComputer went over. 
Computer's hand: {computer_hand}, final score: {sum(computer_hand)}    
YOU WIN :)""")
    return True
  return False

def blackjack():
  
  # Chooses to continue keeps track of till when the while loop needs to run
  chooses_to_continue = True
  
  print(logo)
  
  while chooses_to_continue:
    
    user_score = sum(user_hand)
    
    # After every cycle the user's current score and computer's first card is displayed.
    # User is then given an option whether he'd like to pick a new card or not.
    print(f"Your cards: {user_hand}, current score: {user_score}")
    print(f"Computer's first card: {computer_hand[0]}")
    
    discontinue = game_over(user_score, sum(computer_hand))
    
    if discontinue:
      chooses_to_continue =  False 
    else:
      choice = input("Type 'y' to get another card, 'n' to pass: ")
      
      if choice == 'n':
       
        '''If the user chooses to not add any more cards. 
          Then firstly the computer plays.
          We then look if any of them have gone bust or have a blackjack. If not we check the final scores and declare a winner.'''
        
        computer_plays()
        computer_score = sum(computer_hand)
        result_game_over = game_over(user_score, sum(computer_hand))
        
        if result_game_over == True:
          break
        
        print(f"\nYour final hand: {user_hand}, Your final score: {user_score}")
        print(f"Computer's final hand: {computer_hand}, Your computer's score: {sum(computer_hand)}")
        if (user_score > computer_score):
          print("\nYOU WIN!\n")
        elif user_score < computer_score:
          print("\nYOU LOSE :(\n")
        else:
          print("It's a draw\n")
        
        chooses_to_continue = False
      else:
        user_hand.append(random.choice(cards))

        if 11 in user_hand and user_score > 21:
          user_hand.remove(11)
          user_hand.append(1)
        continue


new_game = True

while new_game: 
  restart = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
  if restart == 'y':
    #clear()
    
    user_hand = []
    computer_hand = []
    
    for i in range(0,2):
      user_hand.append(random.choice(cards))
      computer_hand.append(random.choice(cards))
      if (sum(user_hand) > 21) and (11 in user_hand):
        user_hand = [card.replace(11, 1) for card in user_hand]
      if (sum(computer_hand) > 21) and (11 in computer_hand):
        computer_hand = [card.replace(11, 1) for card in computer_hand]
  
    blackjack()
  else:
    new_game = False
    print("THANK YOU")
