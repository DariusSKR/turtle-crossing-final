from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_RANGE_VALUE = [
    -260, -240, -220, -200, -180, -160, -140, -120, 0, 20, 40, 60, 80, 100,
    120, 140, 160, 180, 200, 220, 240, 260
]
X_RANGE_VALUE = list(range(400, 1200, 60))


class CarManager:

    def __init__(self):
        self.segments = []
        self.speed = 10
        self.create_enemy_car()

    def create_enemy_car(self):
        for _ in range(0, 12):
            self.car = Turtle()
            self.car.penup()
            self.car.speed(self.speed)
            # self.car.pos = 0
            # self.posX = 0
            self.car.goto(random.choice(X_RANGE_VALUE),
                          random.choice(Y_RANGE_VALUE))

            self.car.shape('square')
            self.car.left(180)
            self.car.color(
                'black',
                random.choice(COLORS),
            )
            self.car.shapesize(2, 3, 1)
            self.segments.append(self.car)

    def move(self):
        for _ in range(0, 12):

            self.segments[_].forward(MOVE_INCREMENT)
            # print(self.segments[_].pos)
            if (self.segments[_].pos()[0] <= -300):
                self.segments[_].goto(random.choice(X_RANGE_VALUE),
                                      random.choice(Y_RANGE_VALUE))

    def speed_up(self):
        self.speed += 1
        for _ in range(0, 12):
            self.segments[_].speed(self.speed)

    def reset(self):
        for i in range(0, 12):
            self.segments[i].goto(random.choice(X_RANGE_VALUE),
                                  random.choice(Y_RANGE_VALUE))
