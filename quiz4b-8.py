import simplegui

point_pos = [10 , 20]
change = [1, 0.7]
acc = [0 , 0]
time = 0

def tick():
    global time
    time += 1
    global acc
        
    change[0] += time*acc[0]
    change[1] += time*acc[1]
    
    acc[0] += 1
    acc[1] += 1

def draw_handler(canvas):
    point_pos = [10 , 20]
    
    point_pos[0] += time*change[0]
    point_pos[1] += time*change[1]
    canvas.draw_point(point_pos,'white')
    
frame = simplegui.create_frame('Testing', 500, 500)

frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(1000, tick)
frame.start()
timer.start()