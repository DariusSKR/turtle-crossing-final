import turtle

FONT = ("Courier", 24, "normal")

class Scoreboard:
  def __init__(self):
      self.score = 0
      self.scoreboard = turtle.Turtle()
      self.details()


  def details(self):
      self.scoreboard.penup()
      self.scoreboard.hideturtle()
      self.scoreboard.goto(0,250)
      self.scoreboard.write(self.score,font=FONT)
    
  def increment(self):
    self.score+=1
    self.scoreboard.clear()
    self.scoreboard.write(self.score,font=FONT)
        
  def gameOver(self):
    self.scoreboard.clear()
    self.scoreboard.goto(0,0)
    self.scoreboard.write('GAME OVER',font=FONT)

  def reset(self):
    self.scoreboard.clear()
    self.scoreboard.goto(0,250)
    self.score=0
    self.scoreboard.write(self.score,font=FONT)
    
    
        

