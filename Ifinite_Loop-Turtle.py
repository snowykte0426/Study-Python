import random
import turtle

t = turtle.Turtle()
t.shape("turtle")

for x in range(30):
    length = random.randint(1, 100)
    t.forward(length)
    angle = random.randint(-180, 180)
    t.right(angle)
turtle.mainloop()
turtle.bye()