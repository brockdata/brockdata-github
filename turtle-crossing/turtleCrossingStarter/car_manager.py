from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ACCELERATOR = 1
START_CARS = 20
BOOLS = [True, False]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.start_cars()
        self.new_car_bool = True

    def move_cars(self):
        for c in self.cars:
            # move
            c.forward(self.move_distance)
            # remove when they reach the end
            if c.xcor == 501:
                self.cars.remove(c)

    def start_cars(self):
        for n in range(0, START_CARS):
            car = Turtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.shape('square')
            car.shapesize(stretch_len=2)
            car.goto((random.randint(-500,500), random.randint(-350, 350)))
            self.cars.append(car)

    def new_car(self):
        if self.new_car_bool:
            car = Turtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.shape('square')
            car.shapesize(stretch_len=2)
            car.goto((-500, random.randint(-350,350)))
            self.cars.append(car)
        self.new_car_bool = random.choice(BOOLS)