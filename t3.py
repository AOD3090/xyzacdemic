import turtle as t

t.shape("turtle")

t.bgcolor('black')
t.color('yellow')
t.penup()
t.goto(100,100)
t.pendown()

angle = 90

for x in range(500):
    t.forward(x)
    t.left(angle)

