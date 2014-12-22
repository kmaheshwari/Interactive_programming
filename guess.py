#template for "Guess the number" mini-project
#input will come from buttons and an input field
#all output for the game will be printed in the console
import simplegui
import random
import math

#initialize global variables in your code
num_range = 100
secret_number = 0
count=7

# define event handlers for control panel
def new_game():
    global secret_number
    global count
    count = 7 
    secret_number = random.randrange(0,num_range)
    print "\n \n New game. Range is from 0 to ", num_range  
    print "\nNumber of remaining guesses is ",count
           
def range100():
    #button that changes range to range (0,100) and restarts the game
    global num_range
    global count
    count = 7
    num_range = 100
    new_game()
    
def range1000():
    #button that changes range to range (0,100) and restarts the game
    global num_range
    global count
    count = 10
    num_range = 1000
    new_game()

def get_input(guess):
    # main game logic goes here
    global count
    print "Guess was",guess
    guess = int(guess)
    count = count - 1
    if count < 1:
        print "You ran out of guesses !!. The number was",secret_number
        new_game()
    else:
        if guess > secret_number:
            print "Lower!"
            print "\nNumber of remaining guesses is ",count
            
        elif guess < secret_number:
            print "Higher!\n"
            print "\nNumber of remaining guesses is ",count
            
        else:
            print "Correct! \n"
            new_game()

# create frame
f= simplegui.create_frame("Guess the number", 200, 200)

#register event handlers for control elements
f.add_button("Range is [0, 100]", range100, 200)
f.add_button("Range is [0, 1000]", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

new_game()

# start frame

f.start
# always remember to check your completed program against 
