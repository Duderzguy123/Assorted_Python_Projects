# Color Spiral.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = eval(input("Enter a number of sides between 2 and 6: "))
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(1360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/100)
    t.backward(60)
    
