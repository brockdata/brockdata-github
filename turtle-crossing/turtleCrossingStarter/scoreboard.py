from turtle import Turtle

FONT = ("Calibri", 18, "normal")
TITLE_HEIGHT = 350
SUBTITLE_HEIGHT = TITLE_HEIGHT


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color('white')
        self.level = 0
        self.lives = 3
        self.win = True
        self.update_score()

    def update_score(self):
        self.clear()
        self.sety(TITLE_HEIGHT)
        if self.win == True:
            self.level += 1
        elif self.win == False:
            self.lives -= 1
        self.write(arg=f'Turtle Crossing   Level: {self.level}   Lives: {self.lives}', move=False, align='center',
                   font=FONT)

    def squish(self):
        self.clear()
        self.sety(SUBTITLE_HEIGHT)
        self.write(arg=f'Squished... -1 Life', move=False, align='center', font=FONT)
        self.win = False

    def win_round(self):
        self.clear()
        self.sety(SUBTITLE_HEIGHT)
        self.write(arg=f'Win! Cars move faster...', move=False, align='center', font=FONT)
        self.win = True

    def lose_game(self):
        self.clear()
        self.sety(SUBTITLE_HEIGHT)
        self.write(arg=f'Out of lives... Bring a harder shell next time!', move=False, align='center', font=FONT)

    def win_game(self):
        self.clear()
        self.sety(SUBTITLE_HEIGHT)
        self.write(arg=f'Enough monotony. You WIN!', move=False, align='center', font=FONT)
