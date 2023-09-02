import random
import turtle
t = turtle.Turtle()
t.speed(0)
def star():
  for i in range(5):
    t.fd(10)
    t.right(144)
seed_val = random.randint(1,10000)
print("This seed is",seed_val,)
random.seed(seed_val)
num = random.randint(40,100)
x = [random.randint(-300,300) for i in range(num)]
y = [random.randint(-300,300) for i in range(num)]
for i in range(num):
  t.penup()
  t.goto(x[i],y[i])
  t.pendown()
  star()
