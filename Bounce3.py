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

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = 0
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = 0
        self.y = 0
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
        if self.hit_paddle() == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = -self.x
        if pos [2] >= self.canvas_width:
            self.x = -self.x

    def hit_paddle(self):
        pos = self.canvas.coords(self.id)
        paddle_pos = self.paddle.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def start(self):
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

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

''' bonus class to keep score'''
class Score:
    def __init__(self, canvas, color, ball):
        self.canvas = canvas
        self.ball = ball
        self.id = canvas.create_text(25,10, text = 'Score 0')
        self.points = 0
        self.y = 10

    def draw(self):
        if self.ball.hit_paddle() == True:
            self.points += 1
            self.canvas.itemconfigure(self.id, text= 'Score ' + str(self.points))

def game_start():
    game_running = True
    
    while game_running:
        if ball.hit_bottom == False:
            paddle.draw()
            ball.draw()
            score.draw()
        else:
            game_running = False
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

def end_game():
    end_game = True
    while end_game:
        time.sleep(1)
        canvas.create_text(250, 100, text = 'You scored ' + str(score.points) + ' points!!', font=('Times',20))
        canvas.create_text(250,150, text = 'Game Over!!', font=('Times',20))
        tk.update_idletasks()
        tk.update()
        ball.canvas.move(ball.id, 300, 0)
        time.sleep(3)

        end_game = False



paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
score = Score(canvas, 'black', ball)

btn = Button(tk, text = 'Start Game', command = ball.start)
btn.pack()

time.sleep(1)
game_start()
end_game()

