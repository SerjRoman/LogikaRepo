import turtle

main_turtle = turtle.Turtle()
def figura():
    main_turtle.color("blue")
    main_turtle.penup()
    main_turtle.goto(-50,0)
    main_turtle.pendown()
    for i in range(6):
     main_turtle.forward(100)
     main_turtle.left(60)
figura()
main_turtle.hideturtle()
turtle.exitonclick()