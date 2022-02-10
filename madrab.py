#import turtle module
import turtle

wind=turtle.Screen()#intializ screen
wind.title("ping pang")#set title of game
wind.bgcolor("black")#set color of background
wind.setup(width=800,height=600)#set width and hight of screen
wind.tracer(0)#stop window updating automatically

#madrab 1
madrab1=turtle.Turtle()
madrab1.color("blue")#set color of madrab
madrab1.shape("square")#set shap of madrab
madrab1.penup()#stop object from drwing the lines
madrab1.shapesize(stretch_wid=5,stretch_len=1)#set width and lenth of madrab
madrab1.goto(-350,0)#set position of madrab

#madrab2
madrab2=turtle.Turtle()
madrab2.color("green")
madrab2.shape("square")
madrab2.penup()
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.goto(350,0)

#ball
ball=turtle.Turtle()
ball.color("red")
ball.shape("square")
ball.penup()
ball.goto(0,0)

#move of ball
ball.dx=0.2
ball.dy=0.3

#score
score=turtle.Turtle()
score.speed(0)
score.goto(0,270)
score.color("white")
score.penup()
score.hideturtle()
score.write("player1 : 0 , player2 : 0",align="center",font=("Courier ",18,"normal"))
score1=0
score2=0

#functions
def madrab1_up():
    y=madrab1.ycor()#get y coordinate to madrab1
    y+=30# increas y by 30
    madrab1.sety(y)#set y of madrab1 to the  new y of coordinate
def madrab1_down():
    y=madrab1.ycor()
    y-=30# decreas y by 30
    madrab1.sety(y)
def madrab2_up():
    y=madrab2.ycor()
    y+=30
    madrab2.sety(y)
    if madrab2.ycor()>399:
        y=390
def madrab2_down():
    y=madrab2.ycor()
    y-=30
    madrab2.sety(y)
#keyboard binding

wind.listen()#tell the window to expect keyboard input
wind.onkeypress(lambda :madrab1_up(), "w")#when prassing on w madrab1_up is invoked
wind.onkeypress(lambda :madrab1_down(), "s")
wind.onkeypress(lambda :madrab2_up(), "Up")
wind.onkeypress(lambda :madrab2_down(), "Down")
#main loop of game
while True:
    wind.update()#update the screen everytime oop is run
    #move of ball
    ball.setx(ball.xcor()+ball.dx)#start ball at 0 and everytime loops run increase 0.3 xaxise
    ball.sety(ball.ycor() + ball.dy)#start ball at 0 and everytime loops run increase 0.3 yaxise

    #border check #top order 300px , bottom order -300px ,ball20px
    if ball.ycor()>290:#if ball is at top order
        ball.sety(290)#set y coordanite +290
        ball.dy*=-1#revers direction of ball,make 0.3-->-0.3

    if ball.ycor()<-290:#if ball is at bottom order
        ball.sety(-290)#set y coordanite -290
        ball.dy*=-1#revers direction of ball,make -0.3-->0.3

    if ball.xcor() > 390:# if ball at right order
        ball.goto(0,0)#get ball to center of screen (0,0)
        ball.dx *= -1#revers x direction
        score1+=1
        score.clear()
        score.write(f"player1 : {score1} , player2 : {score2}", align="center", font=("Courier ", 18, "normal"))

    if ball.xcor() < -390:# if ball at left order
        ball.goto(0,0)#get ball to center of screen (0,0)
        ball.dx *=-1#revers x direction
        score2+=1
        score.clear()
        score.write(f"player1 : {score1} , player2 : {score2}", align="center",font=("Courier ", 18, "normal"))


    #hit madrab and ball
    if(ball.xcor()>340 and ball.xcor()<350 and ball.ycor()<madrab2.ycor()+40 and ball.ycor()>madrab2.ycor()-40):
        ball.setx(340)
        ball.dx*=-1

    if (ball.xcor() <-340 and ball.xcor()>-350 and ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1