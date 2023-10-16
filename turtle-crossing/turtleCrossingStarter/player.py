from turtle import Turtle

STARTING_POSITION = (0, -375)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.shape('turtle')
        self.color('white')
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.setheading(NORTH)
        self.forward(10)

    def down(self):
        self.setheading(SOUTH)
        self.forward(10)

    def left(self):
        self.setheading(WEST)
        self.forward(10)

    def right(self):
        self.setheading(EAST)
        self.forward(10)
    def reset_position(self):
        self.goto(STARTING_POSITION)