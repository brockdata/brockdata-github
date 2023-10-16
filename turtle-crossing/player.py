from turtle import Turtle
import constants


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.shape('turtle')
        self.color('white')
        self.setheading(constants.90)
        self.goto(constants.PLAYER_START)

    def up(self):
        self.setheading(constants.NORTH)
        self.forward(10)

    def back(self):
        self.setheading(constants.SOUTH)
        self.forward(10)

    def left(self):
        self.setheading(constants.WEST)
        self.forward(10)

    def right(self):
        self.setheading(constants.EAST)
        self.forward(10)