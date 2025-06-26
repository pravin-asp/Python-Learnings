import turtle
scr = turtle.Screen()
scr.bgcolor('yellow')
line = turtle.Turtle()
line.pensize(5)
line.color('blue')
alin = turtle.Turtle()
alin.pensize(5)
alin.color('red')
alin.shape('spider')
alin.up()
distance = 10
for _ in range(50):
    line.forward(distance)
    alin.stamp()
    alin.forward(distance)
    line.left(60)
    alin.left(60)
    distance += 5
scr.exitonclick()
