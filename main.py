######################################################
# Project: project 2
# UIN: 651525023
# repl.it URL: https://replit.com/@MatthewMohaupt/project-2#main.py
######################################################

#imports
import turtle 
import random

#variables
width = 500
height = 500
pause = True
status = "Play"
distance = 1
score = 0
lives = 3
level = 1


def main():
  
  #make objects
  rando = random.Random()
  s = turtle.Screen()
  player = turtle.Turtle()
  good = turtle.Turtle()
  bad = turtle.Turtle()
  scoret = turtle.Turtle()
  livest = turtle.Turtle()
  levelt = turtle.Turtle()

  #screen stuff
  s.bgpic("background.gif")
  s.screensize(500, 500)
  s.setup(520, 520)
  s.addshape("spaceship.gif")
  s.addshape("asteroid.gif")
  s.addshape("coin.gif")
  s.tracer(0)

#setting up turtle
  player.penup()
  player.shape("spaceship.gif")
  player.goto(0,-250)
  good.penup()
  good.shape("coin.gif")
  good.goto(100, 250)
  bad.penup()
  bad.shape("asteroid.gif")
  bad.goto(-100, 250)
  scoret.penup()
  scoret.hideturtle()
  scoret.color("white")
  livest.penup()
  livest.hideturtle()
  livest.color("#ff2400")
  levelt.penup()
  levelt.hideturtle()
  levelt.color("green")
  

  #methods
  def start():
    global pause
    pause = False

  def stop():
    global pause
    pause = True

  def GameOver():
    global lives
    global distance
    global score
    global level
    distance = 1
    score = 0
    lives = 3
    level = 1

  def right():
    player.setheading(0)
    player.fd(15)

  def left():
    player.setheading(180)
    player.fd(15)

  def nothing():
    player.fd(0)

  def colliding(t1, t2, agree):
    global score
    global lives
    global distance
    global level
    collision = t1.distance(t2)
    if (agree == "Yes"):
      if (collision < 100):
        score += 1
        if (score%3 == 0):
          distance += 0.5
          level += 1
        good.sety(250)
        good.setx(rando.randrange(-250, 250))
    elif (agree == "No"):
      if (collision < 150):
        lives -= 1
        bad.sety(250)
        bad.setx(rando.randrange(-250, 250))

#game loop
  while(status == "Play"):
#determines whether game is in not game over
    if (lives > 0):
      #determines whether the game is paused
      if(pause):
        scoret.goto(-200, 200)
        livest.goto(-200, 100)
        levelt.goto(-200, 0)
        scoret.write("Use the left and right buttons to control the ship")
        livest.write("collect coins and avoid asteroids")
        levelt.write('press the spacebar to start and stop the game')
        s.onkey(start, "space")
        s.listen()
      else:
        #determines whether the game is not paused
        scoret.goto(-200, 200)
        livest.goto(200, 200)
        levelt.goto(0, 200)

        wordscore = str(score)
        wordlives = str(lives)
        wordlevel = str(level)
        currentxp = player.xcor()
        currentyg = good.ycor()
        currentyb = bad.ycor()
        player.clear()
        good.clear()
        bad.clear()
        scoret.clear()
        scoret.write("Score: "+wordscore, False, align = "center", font = ("Arial", 15, "normal"))
        livest.clear()
        livest.write("Lives: "+wordlives, False, align = "center", font = ("Arial", 15, "normal"))
        levelt.clear()
        levelt.write("Level: "+wordlevel, False, align = "center", font = ("Arial", 15, "normal"))

    #controls
        if(currentxp < (width/2)):
          s.onkey(right, "Right")
        else:
          s.onkey(nothing, "Right")
        if(currentxp > -(width/2)):
          s.onkey(left, "Left")
        else:
          s.onkey(nothing, "Left")
        s.onkey(stop, "space")

    #animation of good and bad
        new_yg = currentyg - distance
        new_yb = currentyb - distance
        randoxg = rando.randrange(-250, 250)
        randoxb = rando.randrange(-250, 250)

        if(new_yg < -(height/2)):
          new_yg = currentyg + height
          good.setx(randoxg)
        good.sety(new_yg)

        if(new_yb < -(height/2)):
          new_yb = currentyb + height
          bad.setx(randoxb)
        bad.sety(new_yb)

        colliding(player, good, "Yes")
        colliding(player, bad, "No")
        
          
        s.listen()
        s.update()
    else:
      #game over
      player.clear()
      good.clear()
      bad.clear()
      livest.clear()
      scoret.clear()
      levelt.clear()
      livest.goto(0, 0)
      livest.write("Game Over", move = False, align = "center", font =("Arial", 20, "normal"))
      scoret.goto(0,0)
      scoret.write("to retry press space")
      s.onkey(GameOver, "space")
      s.listen()

main()