import turtle

main_turtle = turtle.Turtle()

def draw_circle(x,y):
    main_turtle.penup()
    main_turtle.goto(x,y)
    main_turtle.pendown()
    main_turtle.color('red')
    main_turtle.begin_fill()
    main_turtle.circle(50)
    main_turtle.end_fill()
draw_circle(100,100)

main_turtle.hideturtle()
turtle.exitonclick()