import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

TITLE_TIME = 50

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.tracer(0)

player = Player()

car_manager = CarManager()

scoreboard = ScoreBoard()

bools = [True, False]

# controls
# no parens in the listen. If you did, it would only trigger when this line of code is run.
screen.listen()
screen.onkey(player.up, 'Up')
screen.onkey(player.down, 'Down')
screen.onkey(player.left, 'Left')
screen.onkey(player.right, 'Right')

game_is_on = True
round_is_on = True
time_count = 0
while game_is_on:
    # move cars
    car_manager.new_car()
    car_manager.move_cars()
    if round_is_on:
        # check out of lives
        if scoreboard.lives <= 0:
            scoreboard.lose_game()
            round_is_on = False
            game_is_on = False
        # check win game
        if scoreboard.level > 5:
            scoreboard.win_game()
            round_is_on = False
            game_is_on = False
        for c in car_manager.cars:
            # check for squish
            if c.distance(player) < 20:
                scoreboard.squish()
                round_is_on = False
        # check finish line
        if player.ycor() >= 400:
            scoreboard.win_round()
            car_manager.move_distance = car_manager.move_distance * scoreboard.level
            round_is_on = False
    else:
        player.reset_position()
    time.sleep(0.1)
    screen.update()
    # timing for subtitles
    if round_is_on == False:
        time_count += 1
        if time_count == TITLE_TIME:
            player.reset_position()
            scoreboard.update_score()
            time_count = 0
            round_is_on = True
    else:
        time_count = 0
