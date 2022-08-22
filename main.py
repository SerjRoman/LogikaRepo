import turtle

main_turtle = turtle.Turtle()
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