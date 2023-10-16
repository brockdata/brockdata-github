import turtle
from turtle import Turtle
import random
import constants

# for random colors
turtle.colormode(255)

# all_cars
all_cars = []


# general functions
def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def rand_speed():
    speed = random.randint(1, 5)
    return speed


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color((255, 255, 255))
        self.shape('square')
        self.shapesize(stretch_len=3)
        self.car_speed = 5
        self.y = 0
        self.group = 'left'
        self.new_car()

    def start_cars(self):
        # create cars
        for n in range(0, constants.START_CARS - 1):
            car = Car()
            car.group = 'left'
            car.y = constants.STARTX_LEFT + (25 * n)
            car.new_car()
            car.heading = constants.EAST
            all_cars.append(car)
        for n in range(0, constants.START_CARS - 1):
            car = Car()
            car.group = 'right'
            car.y = constants.STARTY_RIGHT + (25 * n)
            car.new_car()
            car.heading = constants.WEST
            all_cars.append(car)

    def new_car(self):
        self.car_speed = rand_speed()
        self.color(rand_color())
        if self.group == 'left':
            self.setheading(constants.EAST)
            self.goto((constants.STARTX_LEFT, self.y))
        elif self.group == 'right':
            self.setheading(constants.WEST)
            self.goto((constants.STARTX_RIGHT, self.y))
