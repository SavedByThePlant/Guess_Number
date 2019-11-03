# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

# sets the initial range to 100
global range_is
range_is = 100

# sets the max count per turn as global
global max_count
max_count = int()
#print "INITIALIZE max_count: " + str(max_count)


# sets the guess number as global
global guess_num
guess_num = int()
#print "INITIALIZE guess_num: " + str(guess_num)
    
# helper function to start and restart the game
def new_game(range_is):
    
    global max_count
    
    # print that a new game started and the range
    print "New Game. Range is [0, " + str(range_is) + ")"
    
    # initialize global variables used in your code here
    # establish secret_number
    global secret_number
    secret_number = random.randrange(0,range_is)
    
    # establish first turn
    global guess_num
    guess_num = 0
    
    #print "NEW_GAME SET guess_num: " + str(guess_num)
    #print "NEW_GAME max_count: " + str(max_count)
    # set max number of turns based on range
    
    if range_is == 100:
        max_count = 7
    elif range_is == 1000:
        max_count = 10
    else:
        return
    
    return guess_num
    
# define event handlers for control panel
def range100():
    #print "RANGE100 max_count: " + str(max_count)
    # button that changes the range to [0,100) and starts a new game 
    global range_is
    range_is = 100
    global secret_number
    secret_number = random.randrange(0,100)
    new_game(range_is)
    
def range1000():
    #print "RANGE1000 max_count: " + str(max_count)    
    global range_is
    range_is = 1000
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number = random.randrange(0,1000)
    new_game(range_is)
    
def input_guess(guess):
    
    #print "INPUT_GUESS max_count: " + str(max_count)
    
    global guess_num
    
    #print "INPUT_GUESS BEFORE INC guess_num: " + str(guess_num)
    
    guess_num += 1
    
    #print "INPUT_GUESS AFTER INC guess_num: " + str(guess_num)
    
    guess = int(guess)
    print "   Guess was " + str(guess)
    
    if guess_num < max_count:
        #print "   Secret_number: " + str(secret_number)
        # compare secret_number to guess and print message
        if guess == secret_number:
            print "   Correct"
            #print "STARTING NEW GAME"
            new_game(range_is)
        elif guess < secret_number:
            print "   Higher"
            print "You have " + str(max_count-guess_num) + " guesses remaining."
            return guess_num
        elif guess > secret_number:
            print "   Lower"
            print "You have " + str(max_count-guess_num) + " guesses remaining."
            return guess_num
        else:
            return guess_num  
    else:
        print "You have failed to guess within " + str(max_count) + " guesses."
        new_game(range_is)
# create frame
start_frame = simplegui.create_frame("Guess the Number!", 20, 200, 250)
start_frame.set_canvas_background('dodgerblue')
start_frame.add_input("Guess a number", input_guess, 75)
start_frame.add_button("Range: [0, 100)", range100)
start_frame.add_button("Range: [0, 1000)", range1000)
# register event handlers for control elements and start frame
start_frame.start()

# call new_game 
new_game(range_is) 

# always remember to check your completed program against the grading rubric
