# implementation of card game - Memory

import simplegui
import random

deck1 = range(0,8)
deck2 = range(0,8)
deck1.extend(deck2)
random.shuffle(deck1)
exposed = [False, False, False, False, False,False,False,False,False,False,False, False,False, False,False,False,False, False]
turn = 0
# helper function to initialize globals
def new_game():
    global state,exposed,turn
    state = 0
    random.shuffle(deck1)
    exposed = [False, False, False, False, False,False,False,False,False,False,False, False,False, False,False,False,False, False]
    turn = 0
     
# define event handlers
def mouseclick(pos):
    global deck1,POS,exposed,state,card_1,card_2,turn
    # add game state logic here
    i = pos[0]//50
    if exposed[i] == True:
        return
    else:
        if state == 0:
            exposed[i] = True
            card_1 = i
            state = 1
            
        elif state == 1:
            exposed[i] = True
            card_2 = i
            if deck1[card_1] == deck1[card_2]:
                exposed[card_1] = exposed[card_2] = True
            state = 2
        elif state == 2:
            if deck1[card_1] != deck1[card_2]:
                exposed[card_1]=exposed[card_2]=False
            exposed[i] = True
            card_1 = i
            state = 1
            turn += 1
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global POS,deck1,exposed
    POS = [0,50]
    rec1 = [0,0]
    rec2 = [0,100]
    rec3 = [50,100]
    rec4 = [50,0]
    for j in range(0,16):
        if exposed[j]== False:
            canvas.draw_polygon([rec1, rec2, rec3, rec4], 5, 'Green', 'Brown')
        elif exposed[j] == True:
            canvas.draw_text(str(deck1[j]), POS , 30, 'Red')
        rec1[0] += 50
        rec2[0] += 50
        rec3[0] += 50
        rec4[0] += 50
        POS[0] += 50     
        label.set_text('Turns = ' + str(turn))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric