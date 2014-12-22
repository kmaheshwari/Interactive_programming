# control the velocity of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = 5

# define event handlers
def draw(canvas):
    global vel

    # Draw ball
    canvas.draw_text(str(vel), (20, 20), 12, 'Red')
def keydown(key):
    global vel
    if key==simplegui.KEY_MAP["down"]:
        vel = vel*2
    elif key==simplegui.KEY_MAP["up"]:
        vel = vel - 3
         
    
# create frame 
frame = simplegui.create_frame("Velocity ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
