from vpython import *
import random

time = 0

balls = []

max_lanew=200

colors = [color.red, color.green, color.blue]

number_of_balls = random.randint(100, 150)

for i in range(number_of_balls):
  ball = sphere (pos=vec(random.randint((i*max_lanew+3),(i*max_lanew+max_lanew-3))-(number_of_balls*(max_lanew/2)), random.randint(100,110), 0), radius=random.randint(25,30), color=random.choice(colors))
  balls.append(ball)

while True:
  rate(10)
  time=time+1
  for ball in balls:
    ball.pos.y=ball.pos.y-time*5
    