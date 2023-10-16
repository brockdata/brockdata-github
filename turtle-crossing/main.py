from turtle import Screen
from cars import Car, all_cars
from player import Player
from scoreboard import ScoreBoard
import time
import constants

# screen
screen = Screen()
screen.setup(width=800, height=800)
screen.title('TURTLE CROSSING')
screen.bgcolor('black')
screen.tracer(0)
# score board
scoreboard = ScoreBoard()
# player
timmy = Player()

# controls
screen.listen()
screen.onkey(timmy.up, 'Up')
screen.onkey(timmy.back, 'Down')
screen.onkey(timmy.left, 'Left')
screen.onkey(timmy.right, 'Right')

# game on!
game_on = True
while game_on:
    # move cars
    for c in all_cars:
        c.forward(c.car_speed)
    # remove cars from list when off screen and add new one
    for c in all_cars:
        if c.xcor() > 400 or c.xcor() < -400:
            # add new car
            if c.group == 'left':
                car = Car()
                car.group = 'left'
                car.y = c.ycor()
                car.new_car()
                car.heading = constants.EAST
                all_cars.append(car)
            elif c.group == 'right':
                car = Car()
                car.group = 'right'
                car.y = c.ycor()
                car.new_car()
                car.heading = constants.WEST
                all_cars.append(car)
            all_cars.remove(c)
            c.clear()
            c.ht()

    if scoreboard.detecting:
    # detect collision with car
        for c in all_cars:
            if timmy.distance(c) < 20:
                scoreboard.detecting = False
                scoreboard.win = False
                scoreboard.lives -= 1
                scoreboard.round_over()
        # detect finish line
        if timmy.ycor() >= 400:
            scoreboard.detecting = False
            scoreboard.win = True
            scoreboard.level += 1
        # out of lives
        if scoreboard.lives <= 0:
            scoreboard.detecting = False
            scoreboard.game_over()
    time.sleep(0.01)
    screen.update()

# level_increase and increase speed


screen.exitonclick()
