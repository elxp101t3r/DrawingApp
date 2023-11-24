from turtle import Turtle, Screen
from random import choice
tim = Turtle()
screen = Screen()
tim.shape('arrow')
colors = ['red', 'green', 'blue', 'pink', 'orange', 'purple']
tim.pensize(20)


def move_forwards():
    tim.forward(10)
    tim.color(choice(colors))


def turn_left():
    tim.left(10)
    tim.color(choice(colors))


def turn_right():
    tim.right(10)
    tim.color(choice(colors))


def move_backwards():
    tim.backward(10)
    tim.color(choice(colors))


def clear_window():
    screen.resetscreen()


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_window)


screen.exitonclick()
