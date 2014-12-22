# template for "Stopwatch: The Game"
import simplegui
import time
# define global variables
A = 0
B = 0
C = 0
D = 0
t = 0
x = 0
y = 0
check = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    p = t
    global A, B, C, D
    D = p%10
    p = p/10
    C = p%10
    p = p/10
    if p < 6:
        B = p
    else:
        B = p%6
        A = p/6
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
   
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_handler():
    global check
    timer.start()
    check = 0
    #check = True

def stop_handler():
    global t, x, y, check
    timer.stop()
    check = check + 1
    if check == 1:
        if t%10 == 0:
            x = x + 1
        y = y + 1
        
    
        
def reset_handler():
    global t, x, y
    timer.stop()
    t = 0
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t = t + 1
            
# define draw handler
def draw_handler(canvas):
    global t
    attempts = str(x) + "/" + str(y)
    canvas.draw_text(format(t), [100,150], 36, "Red")
    canvas.draw_text(attempts, [250,20], 30, "Red")
    
# create frame
frame = simplegui.create_frame("Home", 300, 300)
frame.set_draw_handler(draw_handler)
start_button = frame.add_button('Start', start_handler)
stop_button = frame.add_button('Stop', stop_handler)
reset_button = frame.add_button('Reset', reset_handler)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
# start frame
frame.start()

# Please remember to review the grading rubric
