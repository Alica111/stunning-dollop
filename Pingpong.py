from tkinter import*
import random
def spawn_ball():
    global X_SPEED, Y_SPEED
    c.coords(BALL,435,135,465,165)
    X_SPEED=(X_SPEED*SPEED)/abs(X_SPEED)

def bounce(action):
    global X_SPEED,Y_SPEED
    if action=="strake":
        Y_SPEED=random.randrange(-10,10)
        if abs(X_SPEED)<MAX_SPEED:
            X_SPEED=X_SPEED*(-SPEED_UP)
        else:
            X_SPEED=-X_SPEED
    else:
            Y_SPEED=-Y_SPEED
            
    

def move_ball():
    global BALL
    ball_left=c.coords(BALL)[0]
    ball_top=c.coords(BALL)[1]
    ball_right=c.coords(BALL)[2]
    ball_bot=c.coords(BALL)[3]
    ball_center=(c.coords(BALL)[1]+c.coords(BALL)[3])/2
    if ball_right+X_SPEED<right_distance and ball_left+X_SPEED>PAD_W:
        c.move(BALL,X_SPEED,Y_SPEED)
    elif ball_right==right_distance or ball_left==PAD_W:
        if ball_right>450:
            if c.coords(RIGHT_PAD)[1]<ball_center<c.coords(RIGHT_PAD)[3]:
                bounce("strake")
            else:
                spawn_ball()
        else:
            if c.coords(LEFT_PAD)[1]<ball_center<c.coords(LEFT_PAD)[3]:
                bounce("strake")
            else:
                spawn_ball()
    else:
        if ball_right>450:
            c.move(BALL,right_distance-ball_right,Y_SPEED)
        else:
            c.move(BALL,-ball_left+PAD_W,Y_SPEED)
    if ball_top+Y_SPEED<0 or ball_bot+Y_SPEED>300:
        bounce("ricochet")
    root.after(10, move_ball)
        
SPEED_UP=1.05
MAX_SPEED=23

SPEED=10
X_SPEED=10
Y_SPEED=10

PAD_W=10



right_distance=890
root=Tk()
c=Canvas(width=900,height=300,bg='#aa82ff')
c.pack()
c.focus_set()
global BALL
BALL=c.create_oval(435,135,465,165,fill='#efaca3',outline='#efaca3')
c.create_line(10,0,10,300,fill='#85014f')

c.create_line(890,0,890,300,fill='#85014f')

c.create_line(450,0,450,300,fill='#85014f',width=3)
RIGHT_PAD=c.create_rectangle(890,0,900,100,fill='#6d1377',outline='#6d1377')
LEFT_PAD=c.create_rectangle(0,0,10,100,fill='#6d1377',outline='#6d1377')

c.bind('<Up>',lambda event:c.move(RIGHT_PAD,0,-15))
c.bind('<Down>',lambda event:c.move(RIGHT_PAD,0,15))
c.bind('<w>',lambda event:c.move(LEFT_PAD,0,-15))
c.bind('<s>',lambda event:c.move(LEFT_PAD,0,15))

move_ball()















