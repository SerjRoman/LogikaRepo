import turtle

main_turtle = turtle.Turtle()

def Pentagon(x, y):

    main_turtle.color("red")

    main_turtle.penup()
    main_turtle.goto(x, y)
    main_turtle.pendown()

    for i in range(5):
        main_turtle.forward(100)
        main_turtle.left(72)
    
Pentagon(-200, -200)

main_turtle.hideturtle()
turtle.exitonclick()
