import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



#Creating the screen
screen = Screen()
screen.setup(width=1000, height=600)
screen.tracer(0)
screen.listen()
screen.title('Cross the Road by Darius')
screen.bgpic('chicken-crossing-the-road2.gif')
#creating the objects
scoreBoard = Scoreboard()

boby = Player()

enemy = CarManager()

#adding Key-Up move
screen.onkeypress(boby.move, 'Up')


#The game starts
def game():
    game_is_on = True
    while game_is_on:
        #every 100ms re-rendering the screen
        time.sleep(0.2)
        screen.update()
        enemy.move()

        #checking if our boby crashes with the other cars vroom vroom
        for i in range(0, 12):
            if (int(enemy.segments[i].pos()[0]) == int(boby.segment.pos()[0])
                    and int(enemy.segments[i].pos()[1]) == int(
                        boby.segment.pos()[1])
                    or int(enemy.segments[i].pos()[0]) - 10
                    == int(boby.segment.pos()[0]) + 10
                    and int(enemy.segments[i].pos()[1]) == int(
                        boby.segment.pos()[1])
                    or int(enemy.segments[i].pos()[0]) - 10
                    == int(boby.segment.pos()[0]) + 10
                    and int(enemy.segments[i].pos()[1]) - 10
                    == int(boby.segment.pos()[1]) + 10
                    or int(enemy.segments[i].pos()[0]) + 10
                    == int(boby.segment.pos()[0]) - 10
                    and int(enemy.segments[i].pos()[1]) - 10
                    == int(boby.segment.pos()[1]) + 10):
                      
                scoreBoard.gameOver()
                game_is_on = False

    #incrementing the score for each finish line crossed
        if (boby.pos >= 280):
            print('Good boy!')
            enemy.speed_up()
            scoreBoard.increment()
            boby.pos = 0
            boby.segment.goto(0, -280)


game()


#Reseting the game
def reset():
    boby.reset()
    scoreBoard.reset()
    enemy.reset()
    game()


screen.onkeypress(reset, 'Down')
