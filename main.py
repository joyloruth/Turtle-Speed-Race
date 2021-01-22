import turtle
from random import randint

#CREATE BACKGROUND SKY
def screen():
  wn = turtle.Screen()
  wn.bgcolor('skyblue')

#create clouds
#def cloud():
  #cloud = turtle.Turtle()
  #cloud.hideturtle()
  #cloud.penup()
  #cloud.forward(5)
  #cloud.right(5)
  #cloud.color('white')


#CREATE BORDER
def border():
  border = turtle.Turtle()
  border.color('black')
  border.hideturtle()
  border.penup()
  border.goto(-300,155)
  border.setheading(90)
  border.pensize(3)
  border.speed(9)
  
  for number in range(2):    
    border.begin_fill()
    border.pendown()
    border.right(90)
    border.forward(600)
    border.right(90)
    border.forward(310)
    border.end_fill()

#border_line

def border_line():
  border_line = turtle.Turtle()
  border_line.color('gray')
  border_line.hideturtle()
  border_line.penup()
  border_line.goto(-300,155)
  border_line.setheading(90)
  border_line.pensize(13)
  border_line.speed(9)
  
  for number in range(1):
    border_line.pendown()
    border_line.right(90)
    border_line.forward(600)
    border_line.right(90)
    border_line.forward(320)
    border_line.right(90)
    border_line.forward(600)
    border_line.right(90)

  for number in range(5):
    border_line.pensize(5)
    border_line.forward(20)
    border_line.right(90)
    
    border_line.forward(600)
    border_line.pendown()
    border_line.left(90)
    
    border_line.pensize(8)
    border_line.forward(40)
    border_line.pensize(9)

    border_line.left(90)

    border_line.forward(600)
    border_line.right(90)

def wall1():
  wall1 = turtle.Turtle()
  wall1.speed(9)
  wall1.penup
  wall1.color('green')
  wall1.pensize(15)
  
  
  wall1.penup()
  wall1.goto(-302,-155)
  wall1.setheading(0)
  wall1.pendown()


  for line in range(6):
    wall1.setheading(0)
    for line in range(60):
      wall1.speed(9)
      wall1.penup()
      wall1.forward(5)
      wall1.pendown()
      wall1.forward(5)
      wall1.penup()
    wall1.backward(600)
    wall1.setheading(90)
    wall1.forward(60)


#create wall
def wall():
  wall = turtle.Turtle()
  wall.speed(0)
  wall.penup
  wall.color('lime')
  wall.pensize(5.5)
  
  
  wall.penup()
  wall.goto(-302,-155)
  wall.setheading(0)
  wall.pendown()


  for line in range(6):
    wall.setheading(0)
    for line in range(60):
      wall.speed(9)
      wall.penup()
      wall.forward(5)
      wall.pendown()
      wall.forward(5)
      wall.penup()
    wall.backward(600)
    wall.setheading(90)
    wall.forward(60)
    
#CREATES STREET PAVEMENT DASHES
def dash():
  
  dash = turtle.Turtle()
  dash.speed(9)
  dash.penup
  dash.color('yellow')
  dash.pensize(2)
  
  
  dash.penup()
  dash.goto(-302,-125)
  dash.setheading(0)
  dash.pendown()


  for line in range(5):
    dash.setheading(0)
    for line in range(60):
      dash.speed(0)
      dash.penup()
      dash.forward(5)
      dash.pendown()
      dash.forward(5)
      dash.penup()
    dash.backward(601)
    dash.setheading(90)
    dash.forward(60)
    dash.hideturtle()


screen()
border()
dash()
wall1()
wall()
border_line()


#PLAYER1
  #CREATE DAISY'S PLATFORM

def platforms():  
  daisyplatform = turtle.Turtle()
  daisyplatform.penup()
  daisyplatform.color('gray')
  daisyplatform.fillcolor('lightgray')
  daisyplatform.pensize(2)
  daisyplatform.shape('circle')

  daisyplatform.penup()
  daisyplatform.speed()
  daisyplatform.goto(-302,-116)
  daisyplatform.setheading(0)
  daisyplatform.pendown()

#CREATE MARIO PLATFORM
  marioplatform = turtle.Turtle()
  marioplatform.penup
  marioplatform.color('gray')
  marioplatform.fillcolor('lightgray')
  marioplatform.pensize(2)
  marioplatform.shape('circle')

  marioplatform.penup()
  marioplatform.speed(0)
  marioplatform.goto(-302,-100)
  marioplatform.setheading(0)
  marioplatform.pendown()


#CREATES WARIO TURTLE RACER
wario = turtle.Turtle()
wario.penup()
wario.color('lightpurple')
wario.fillcolor('purple')
wario.pensize(2)
wario.shape('turtle')
wario.goto(-302,60)
wario.speed()

#CREATES DAISY TURTLE RACER
daisy = turtle.Turtle() 
daisy.penup()
daisy.color('red')
daisy.fillcolor('pink')
daisy.pensize(2)
daisy.shape('turtle')
daisy.goto(-302,-05)
daisy.speed(0)
     
#CREATES MARIO TURTLE RACER    
mario = turtle.Turtle()
mario.penup()
mario.color('blue')
mario.fillcolor('skyblue')
mario.pensize(2)
mario.shape('turtle')
mario.goto(-302,-65)
mario.speed()

#CREATES LUIGI TURTLE RACER
luigi = turtle.Turtle() 
luigi.penup()
luigi.color('orange')
luigi.fillcolor('yellow')
luigi.pensize(2)
luigi.shape('turtle')
luigi.goto(-302,-125)
luigi.speed(0)
     


for turn in range(1):
  daisy.penup()
  mario.penup()
  daisy.showturtle()
 
for turn in range(165):
  wario.forward(randint(3,4))
  daisy.forward(randint(3,4))
  mario.forward(randint(3,4))
  luigi.forward(randint(3,4))

for turn in range(175):
  wario.setheading(180)
  wario.forward(randint(1,5))
  daisy.setheading(180)
  daisy.forward(randint(1,5))
  mario.setheading(180)
  mario.forward(randint(1,5))
  luigi.setheading(180)
  luigi.forward(randint(1,5))


  
  


