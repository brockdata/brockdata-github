from turtle import Turtle
import time


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.level = 0
        self.win = True
        self.detecting = True
        self.lives = 3
        self.ht()
        self.update_score()

    def update_score(self):
        self.clear()
        self.sety(350)
        if self.win == True:
            self.level += 1
        elif self.win == False:
            self.lives -= 1
        self.write(arg=f'Level: {self.level}       Lives: {self.lives}', move=False, align='center',
                   font=('Calibri', 20, 'normal'))

    def round_over(self):
        self.clear()
        self.sety(0)
        if self.win == True:
            self.write(arg=f'ROUND OVER\nNext Level', move=False, align='center', font=('Calibri', 20, 'normal'))
        elif self.win == False:
            self.write(arg=f'ROUND OVER\nSquished... -1 Life\n', move=False, align='center', font=('Calibri', 20, 'normal'))
        self.win = False
        self.update_score()

    def game_over(self):
        self.clear()
        self.sety(0)
        self.write(arg=f'GAME OVER\nFinished Level: {self.level}', move=False, align='center', font=('Calibri', 20, 'normal'))
