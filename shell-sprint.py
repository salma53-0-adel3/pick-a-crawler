import random 
import time
from turtle import Turtle, Screen 
window = Screen() 
window.bgcolor("DarkOliveGreen3")
window.setup(width=600, height=600)
colors = ["green", "pink", "purple"]
go = [0, 200, -200]
turtles = []
winner = []
speed = ["fastest", "fast", "slow", "slowest"]
for t in range(3) :
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.goto(x= -285, y= go[t])
    turtles.append(new_turtle)

def start_race() :
    race = True
    while race :
        for x in turtles :
            if x.xcor() > 268 :
                winner.append(x.pencolor())
                race = False
                break
            for _ in range(1) :
                x.speed(random.choice(speed))
                x.forward(random.randint(1,8))

def display_winner(user, color) :
    x = Turtle()
    x.hideturtle()
    x.penup()
    x.goto(-200,0)
    x.pendown()
    x.color("White")
    time.sleep(2)
    for s in turtles :
        s.hideturtle()
    if user == color :
        window.bgcolor("Red")
        x.write("Woooow you Win!",font=("arial", 30, "bold"))
    else :
        window.bgcolor("blue3")
        x.write("You Lose :(",font=("arial", 30, "bold")) 

while True :
  race_user = window.textinput(title="Turtle race",prompt="Guess the winner\nGreen, Purple, Pink").lower().strip()
  if race_user not in ["green","pink","purple"] : continue
  else :
      start_race()
      display_winner(race_user,winner[0])
      break

window.exitonclick()