from vpython import *
import random

time = 0
falling = True
balls = []
vel = 0
max_lanew=200

colors = [color.red,color.green,color.blue,color.cyan,color.magenta,color.yellow,color.white,color.black,color.orange,color.purple]

number_of_balls = random.randint(50,70)

for i in range(number_of_balls):
  ball = sphere (pos=vec(random.randint((i*max_lanew+3),(i*max_lanew+max_lanew-3))-(number_of_balls*(max_lanew/2)), random.randint(100,110), 0), radius=random.randint(25,30), color=random.choice(colors))
  balls.append(ball)

while True:
  rate(10)
  if (falling == True):
    time=time+1
    for ball in balls:
      if (ball.pos.y<-3000):
        falling = False
        vel = random.randint(1,5)*time
      else:
        vel = -time*5
        ball.pos.y=ball.pos.y + vel
  else:
    time=time+1
    for ball in balls:
      if (ball.pos.y>3000):
        falling = True
        vel = -time*5
      else:
        vel = random.randint(1,5)*time
        ball.pos.y=ball.pos.y + vel