import turtle

main_turtle = turtle.Turtle()

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



main_turtle.hideturtle()
turtle.exitonclick()