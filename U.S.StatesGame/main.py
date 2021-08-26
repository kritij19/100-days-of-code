from turtle import Turtle, Screen
import pandas as pd

# Turtle only accepts images in .gif format
image = r'us-states-game-start\blank_states_img.gif'
states_csv_path = r'us-states-game-start\50_states.csv'

screen = Screen()
screen.title('U.S States Game')

# Making a turtle object in the shape of the image
screen.addshape(image)
Turtle().shape(image)

# Getting list of all states.
states_data = pd.read_csv(states_csv_path)
states_list = states_data.state.to_list()   

game_is_on = True
guessed_correctly = 0

while game_is_on:
  
    # Game over when all guessed
    if guessed_correctly != 50:

        # Taking input from user
        user_answer = screen.textinput(f"{guessed_correctly}/50 Guessed", prompt = "Enter the name of a state: ")
        user_answer_titlecased = user_answer.title()

        if user_answer_titlecased == 'Exit':
            game_is_on = False
        
        # Checking if guess exists in state_list
        if user_answer_titlecased in states_list:

            turtle = Turtle()
            turtle.hideturtle()
            turtle.penup()
            turtle.color('black')

            # Writing state name at correct coordinates
            row = states_data.loc[states_data['state'] == user_answer_titlecased]
            turtle.goto(int(row.x), int(row.y))
            turtle.write(f"{user_answer}")
            
            # Removing guessed guessed states from list
            states_list.remove(user_answer_titlecased)
            guessed_correctly += 1

    else:
        game_is_on = False

# Csv of all missed states
missed_states_dict = {'states': states_list}
missed_states_df = pd.DataFrame(missed_states_dict)
missed_states_df.to_csv('missed_states.csv')

screen.exitonclick()
