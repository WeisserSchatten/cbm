import turtle

window = turtle.Screen()
t = turtle.Turtle()

for c in ['red', 'green', 'yellow', 'blue']:
    t.color(c)
    t.forward(75)
    t.left(90)

t.pos()
window.exitonclick()
