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



TurtLe(100,100)
main_turtle.hideturtle()
turtle.exitonclick()