import turtle

main_turtle = turtle.Turtle()

def ilya(x,y):
    main_turtle.penup()
    main_turtle.goto(x, y)
    main_turtle.pendown()
    main_turtle.begin_fill()
    main_turtle.fillcolor('black')
    main_turtle.forward(50)
    main_turtle.left(135)
    main_turtle.forward(70)
    main_turtle.left(135)
    main_turtle.forward(50)
    main_turtle.end_fill()
    
ilya(100,100)



main_turtle.hideturtle()
turtle.exitonclick()