from Tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 500,height = 400, bd = 0, highlightthickness=0)
canvas.pack()
tk.update()

points = 0

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = 0
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id,245, 100)
    	starts = [-3,-2,-1,0,1,2,3]
    	random.shuffle(starts)
    	self.x = starts[0]
    	self.y = -3
    	self.canvas_height = self.canvas.winfo_height()
    	self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
        	self.y = 3
        if pos[3] >= self.canvas_height:
        	self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
            self.score += 1
            print self.score 
        if pos[0] <= 0:
        	self.x = -self.x
        if pos [2] >= self.canvas_width:
        	self.x = -self.x

    def hit_paddle(self,pos):
        paddle_pos = self.paddle.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color) # paddle is a blue rectangle
        self.canvas.move(self.id,200,300)  #initial paddle position
        self.x = 0  #direction and speed paddle is moving
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left) #change paddle direction on pressing left key
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right) # other direction
        #self.canvas.bind_all('<Button1>', self.click_mouse)
    def draw(self):
        self.canvas.move(self.id, self.x, 0) # will move in x direction, not in y direction
        pos = self.canvas.coords(self.id) #get coords to variable pos
        if pos[0] <= 0:
            self.x = 0  #stop moving when left side hits left edge
        elif pos[2] >= self.canvas_width:
            self.x = 0 #stop moving when right side hits right edge

    def turn_left(self,evt):
        self.x = -2 #move left when evt is left key is pressed

    def turn_right(self, evt):
        self.x = 2  #move right when evt is right key is pressed
    
    ''' unfinished?  to start the game with a click? evt should be changed to click mouse'''
    def click_mouse(self, evt):  
        self.startgame = True

''' bonus class to keep score'''
class Score:
    def __init__(self, canvas, color, ball):
        self.canvas = canvas
        self.ball = ball
        self.id = canvas.create_text(15,10, text = 'Score 0')
        self.points = 0
        self.y = 10
    
    def draw(self):
        ball_pos = self.ball.canvas.coords(self.id)
        self.canvas.create_text(40, self.y, text = 'Score' + str(self.points))


'''
    def hit_paddle(self, ball_pos):
        paddle_pos = self.ball.paddle.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
'''
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
score = Score(canvas, 'black',ball)

time.sleep(1)

while True:
    if ball.hit_bottom == False:
        paddle.draw()
        ball.draw()
        score.draw()

    else:
        print 'Game Over!!'
        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
