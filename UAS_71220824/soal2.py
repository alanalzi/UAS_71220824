import turtle
s = turtle.Screen()
t = turtle.Turtle()
#background
t.fillcolor("yellow")
t.begin_fill()
turtle.bgcolor("pink")
#kotak kuning
t.fillcolor("yellow")
t.begin_fill()
t.pencolor("yellow")
t.penup()
t.goto(0,0)
t.pendown()
t.right(55)
t.forward(40)
t.left(55)
t.forward(300)
t.left(55)
t.forward(40)
t.left(35)
t.forward(200)
t.left(35)
t.forward(40)
t.left(55)
t.forward(300)
t.left(55)
t.forward(40)
t.left(35)
t.forward(200)
t.penup()
t.end_fill()
#persegi bawah
t.fillcolor("brown")
t.begin_fill()
t.goto(160,-110)
t.pencolor("brown")
t.pendown()
t.left(180)
t.forward(75)
t.right(90)
t.forward(27)
t.right(90)
t.forward(75)
t.right(90)
t.forward(27)
t.end_fill()
#circle
t.penup()
t.goto(180,150)
t.pendown()
t.pensize(5)
t.color("blue")
t.circle(50,360)
#HI
t.penup()
t.goto(140,40)
t.pendown()
t.color("red")
t.left(90)
t.forward(60)
t.penup()
t.goto(140,10)
t.pendown()
t.left(90)
t.forward(40)
t.penup()
t.goto(180,40)
t.pendown()
t.right(90)
t.forward(60)
t.penup()
t.goto(200,40)
t.pendown()
t.forward(60)
#!
t.penup()
t.goto(230,40)
t.pendown()
t.forward(50)
t.penup()
t.goto(228,-20)
t.pendown()
t.circle(3)
turtle.exitonclick()
