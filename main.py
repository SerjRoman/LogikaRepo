import turtle

main_turtle = turtle.Turtle()

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
main_turtle.hideturtle()
turtle.exitonclick()