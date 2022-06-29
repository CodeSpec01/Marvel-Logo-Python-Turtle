# Importing Turtle Module -----------------------------------------------------------------------------------------------
import turtle

# Creating the Window -------------------------------------------------------------------------------------------------

wn = turtle.Screen()
turtle.colormode(255)
wn.bgcolor(205,1,2)
wn.title("Turtle")
m = turtle.Turtle()
white = (194,235,255)
red = (205,1,2)

# Starting of M -------------------------------------------------------------------------------------------------------------------

m.penup()
m.goto(-500,-100)
m.pendown()

m.fillcolor(white)
m.begin_fill()

m.left(90)
m.forward(200)
m.right(90)
m.forward(40)
m.right(65)
m.forward(130)
m.left(130)
m.forward(130)
m.right(65)
m.forward(40)
m.right(90)
m.forward(200)

m.end_fill()

m.penup()
m.right(90)
m.forward(190)
m.pendown()

m.fillcolor(red)
m.begin_fill()

m.backward(40)
m.right(90)
m.forward(118)
m.right(155)
m.forward(130)
m.left(130)
m.forward(130)
m.right(155)
m.forward(118)
m.left(90)
m.forward(40)

m.end_fill()

# Going for the A -----------------------------------------------------------------------------------------------------------------------------------

m.penup()
m.forward(40)
m.pendown()

m.fillcolor(white)
m.begin_fill()

m.left(80)
m.forward(200)
m.right(80)
m.forward(80)
m.right(80)
m.forward(200)
m.right(100)
m.forward(40)
m.right(80)
m.forward(35)
m.left(80)
m.forward(55)
m.left(80)
m.forward(35)
m.right(80)
m.forward(40)

m.end_fill()

m.penup()
m.backward(108)
m.right(80)
m.forward(35)
m.forward(40)
m.pendown()

m.fillcolor(red)
m.begin_fill()

m.forward(65)
m.left(80)
m.forward(20)
m.left(80)
m.forward(65)
m.left(100)
m.forward(42)

m.end_fill()

# Going For the R -------------------------------------------------------------------------------------------------------------------------------

m.penup()
m.forward(40)
m.right(80)
m.forward(75)
m.left(80)
m.forward(40)
m.pendown()

m.fillcolor(white)
m.begin_fill()

m.left(90)
m.forward(200)
m.right(90)
m.forward(30)
m.circle(-60,150)
m.left(90)
m.forward(100)
m.right(120)
m.forward(33)
m.right(60)
m.forward(92)
m.left(150)
m.forward(80)
m.right(90)
m.forward(30)

m.end_fill()

m.penup()
m.right(90)
m.forward(170)
m.right(90)
m.forward(30)
m.pendown()

m.fillcolor(red)
m.begin_fill()

m.circle(-30,180)
m.right(90)
m.forward(60)

m.end_fill()

# Going for the V -----------------------------------------------------------------------

m.penup()
m.backward(170)
m.right(90)
m.forward(90)
m.left(90)
m.forward(200)
m.right(170)
m.pendown()

m.fillcolor(white)
m.begin_fill()

m.forward(203)
m.left(80)
m.forward(70)
m.left(80)
m.forward(203)
m.left(100)
m.forward(40)
m.left(80)
m.forward(144)
m.right(80)
m.forward(10)
m.right(80)
m.forward(144)
m.left(80)
m.forward(40)

m.end_fill()

# Going for the E -------------------------------------------------------------------------

m.penup()
m.backward(140)
m.right(90)
m.backward(200)
m.right(90)
m.forward(40)
m.left(90)
m.pendown() 

m.begin_fill()

m.forward(200)
m.right(90)
m.forward(95)
m.right(90)
m.forward(35)
m.right(90)
m.forward(55)
m.left(90)
m.forward(50)
m.left(90)
m.forward(55)
m.right(90)
m.forward(35)
m.right(90)
m.forward(55)
m.left(90)
m.forward(45)
m.left(90)
m.forward(55)
m.right(90)
m.forward(35)
m.right(90)
m.forward(95)

m.end_fill()

# Going fot the L ------------------------------------------------------------------------

m.penup()
m.right(180)
m.forward(135)
m.left(90)
m.pendown() 

m.begin_fill()

m.forward(200)
m.right(90)
m.forward(40)
m.right(90)
m.forward(160)
m.left(90)
m.forward(100)
m.right(90)
m.forward(40)
m.right(90)
m.forward(140)

m.end_fill()

turtle.done()
