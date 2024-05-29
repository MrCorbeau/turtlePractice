from turtle import *
from random import *

scr = Screen()
scr.setup(width=500, height=500)

bet = scr.textinput(title="MAKE YOUR BET", prompt="Which turtle will win? Donatello, Raphael, Leonardo or Michelangelo :").lower()

if bet == "donatello":
    bet="purple"
elif bet == "raphael":
    bet="red"
elif bet == "leonardo":
    bet="blue"
elif bet == "michelangelo":
    bet="orange"
    
#Donatello
donatello = Turtle(shape="turtle")
donatello.penup()
donatello.color("purple")
donatello.goto(x=-240, y=90)

#Raphael
raphael = Turtle(shape="turtle")
raphael.penup()
raphael.color("red")
raphael.goto(x=-240, y=30)

#Leonardo
leonardo = Turtle(shape="turtle")
leonardo.penup()
leonardo.color("blue")
leonardo.goto(x=-240, y=-30)

#Michelangelo
michelangelo = Turtle(shape="turtle")
michelangelo.penup()
michelangelo.color("orange")
michelangelo.goto(x=-240, y=-90)

race = False

if bet:
    race = True

while race:
    rand = Random()
    step = rand.randint(0, 10)

    winner = ""

    tmnt = [donatello, raphael, leonardo, michelangelo]
    shuffle(tmnt)

    for turtle in tmnt:
        turtle.forward(step*4)
        if turtle.xcor() > 230:
            race = False
            winner = turtle.pencolor()
            if bet == winner:
                print("You Win")
            else:
                print("You Lose")
        break



scr.exitonclick()
