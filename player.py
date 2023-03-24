from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

  def __init__(self):
    self.segment =Turtle()
    self.pos = 0 
    self.configure_turtle()


  def configure_turtle(self):
    self.segment.penup()
    self.segment.shape('square')
    self.segment.color('green')
    self.segment.left(90)
    self.segment.goto(STARTING_POSITION)
    
  def move(self):
    self.segment.forward(MOVE_DISTANCE)
    self.pos=self.segment.pos()[1]

  def reset(self):
    self.segment.goto(STARTING_POSITION)

    # print(self.segment.pos()[1])
