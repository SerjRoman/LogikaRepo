import turtle

main_turtle = turtle.Turtle()

def ilya():
    main_turtle.goto(200, 200)
    main_turtle.begin_fill()
    main_turtle.color(0, 0, 0)
    main_turtle.fillcolor(0, 0, 0)
    main_turtle.pendown()
    main_turtle.left(45)
    main_turtle.forward(50)
    main_turtle.left(225)
    main_turtle.forward(50)
    main_turtle.left(90)
    main_turtle.forward(50)
    main_turtle.end_fill()
    main_turtle.penup()




main_turtle.hideturtle()
turtle.exitonclick()