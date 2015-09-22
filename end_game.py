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

def end_game():
    end_game = True
    while end_game:
        time.sleep(1)
        canvas.create_text(150, 100, text = 'You scored ' + str(score.points) + ' points!!', Font=('Times',20)
        canvas.create_text(150,150, text = 'Game Over!!')
        tk.update_idletasks()
        tk.update()
        ball.canvas.move(ball.id, 300, 0)
        time.sleep(3)

        end_game = False

end_game()




