import turtle

main_turtle = turtle.Turtle()

def rarka():
    main_turtle.penup()
    main_turtle.goto(100,100)
    main_turtle.shapesize(3)
    main_turtle.color("green")
    main_turtle.pendown()
    main_turtle.forward(100)
    main_turtle.right(180)
    main_turtle.right(50)
    main_turtle.forward(70)
    main_turtle.left(95)
    main_turtle.forward(80)


rarka()

main_turtle.hideturtle()
turtle.exitonclick()