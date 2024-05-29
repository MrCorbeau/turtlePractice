from turtle import *

donatello = Turtle()
screen = Screen()
donatello.speed("fastest")

def walk_forward():
    donatello.forward(10)

def walk_backwards():
    donatello.backward(10)

def turn_right():
    donatello.right(30)

def turn_left():
    donatello.left(30)

def restart():
    donatello.reset()

screen.listen()

screen.onkey(key="w", fun=walk_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=walk_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="r", fun=restart)


screen.exitonclick()
    