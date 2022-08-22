import turtle

main_turtle = turtle.Turtle()

def draw_circle():
    main_turtle.penup()
    main_turtle.goto(0,0)
    main_turtle.pendown()
    main_turtle.color('red')
    main_turtle.begin_fill()
    main_turtle.circle(100)
    main_turtle.end_fill()
draw_circle()

main_turtle.hideturtle()
turtle.exitonclick()