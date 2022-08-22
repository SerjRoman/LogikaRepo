import turtle

main_turtle = turtle.Turtle()

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


rarka(100,100)

main_turtle.hideturtle()
turtle.exitonclick()