
import turtle

main_turtle = turtle.Turtle()

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

main_turtle.hideturtle()
turtle.exitonclick()