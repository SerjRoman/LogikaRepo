
import turtle

main_turtle = turtle.Turtle()

def TurtLe(x,y):
    main_turtle.pencolor('blue')
    main_turtle.width(5)
    
    main_turtle.penup()
    main_turtle.goto(x,y)
    main_turtle.pendown()
    
    main_turtle.begin_fill()
    main_turtle.left(90)
    main_turtle.forward(50)
    main_turtle.left(90)
    main_turtle.forward(100)
    main_turtle.left(90)
    main_turtle.forward(50)
    main_turtle.left(90)
    main_turtle.forward(100)
    main_turtle.fillcolor('blue')
    main_turtle.end_fill()


def rarka(x,y):
    main_turtle.penup()
    main_turtle.goto(x,y)
    main_turtle.shapesize(3)
    main_turtle.color("green")
    main_turtle.pendown()
    main_turtle.forward(50)
    main_turtle.left(120)
    main_turtle.forward(50)
    main_turtle.left(120)
    main_turtle.forward(50)

def YarikTelius(x,y):
    main_turtle.width(7)
    
    main_turtle.color("yellow")
    main_turtle.penup()
    main_turtle.goto(x,y)
    main_turtle.pendown()
    main_turtle.forward(50)
    main_turtle.left(105)
    main_turtle.forward(35)
    main_turtle.left(75)
    main_turtle.forward(35)
    main_turtle.left(75)
    main_turtle.forward(35)


def ilya(x,y):
    main_turtle.penup()
    main_turtle.goto(x, y)
    main_turtle.pendown()
    main_turtle.begin_fill()
    main_turtle.fillcolor('black')
    main_turtle.forward(50)
    main_turtle.left(135)
    main_turtle.forward(70)
    main_turtle.left(135)
    main_turtle.forward(50)
    main_turtle.end_fill()
    
ilya(100,100)


YarikTelius(50,50)


def figura(x,y):
    main_turtle.color("blue")
    main_turtle.penup()
    main_turtle.goto(x,y)
    main_turtle.pendown()
    for i in range(6):
        main_turtle.forward(100)
        main_turtle.left(60)
figura(100,100)


def Turtle(x,y):
    main_turtle.penup()
    main_turtle.goto(x, y)
    main_turtle.pendown()
    main_turtle.left(45)
    main_turtle.width(6)
    for el in range(4):
        main_turtle.forward(100)
        main_turtle.left(90)


Turtle(100,100)

rarka(100,100)


def draw_circle(x,y):
    main_turtle.penup()
    main_turtle.goto(x,y)
    main_turtle.pendown()
    main_turtle.color('red')
    main_turtle.begin_fill()
    main_turtle.circle(50)
    main_turtle.end_fill()
draw_circle(100,100)

def purple_figure(x, y):
    main_turtle.color('purple')
    main_turtle.width(5)
    
    main_turtle.penup()
    main_turtle.goto(x,y)
    main_turtle.pendown()
    
    main_turtle.forward(50)
    main_turtle.left(70)
    main_turtle.forward(50)
    main_turtle.forward(25)
    main_turtle.left(20)
    main_turtle.left(90)
    main_turtle.forward(50)
    main_turtle.left(70)
    main_turtle.forward(50)
    main_turtle.forward(25)

TurtLe(100,100)


def bogdans_pyatiugolnik(x,y):
    main_turtle.color('green')
    main_turtle.penup()
    main_turtle.goto(x,y)
    main_turtle.pendown()
    main_turtle.begin_fill()
    main_turtle.forward(50)
    main_turtle.right(45)
    main_turtle.forward(33)
    main_turtle.right(90)
    main_turtle.forward(33)
    main_turtle.right(45)
    main_turtle.forward(50)
    main_turtle.right(90)
    main_turtle.forward(50) 
    main_turtle.end_fill()   
bogdans_pyatiugolnik(0,0)

main_turtle.hideturtle()
turtle.exitonclick()