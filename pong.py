import turtle
#import os

wn = turtle.Screen()
wn.title("Pong by HarmitJasani")
wn.bgcolor("Black")
wn.setup(800,600)
wn.tracer(0)

#score keeping
score_a=0
score_b=0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

#pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Player A: 0      Player B: 0", align="center", font=("Courier", 24,"normal"))

def paddle_A_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_A_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_A_up,"w")
wn.onkeypress(paddle_A_down,"s")

def paddle_B_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_B_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_B_up,"Up")
wn.onkeypress(paddle_B_down,"Down")


while(True):
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border check

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
        #os.system("start bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
        #os.system("start bounce.wav&")

    if(ball.xcor()>390):
        ball.goto(0,0)
        ball.dx*=-1
        score_a=score_a+1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b),align="center", font=("Courier", 24, "normal"))

    if (ball.xcor()<-390):
        ball.goto(0, 0)
        ball.dx *= -1
        score_b = score_b + 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    # paddle and ball collision

    if ball.xcor()> 340 and ball.xcor()<350 and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

