import turtle
from playsound import playsound # to play audio files
wn=turtle.Screen();
wn.title("Old School Pong");
wn.bgcolor("black");
wn.tracer(0);
wn.setup(width=800,height=600);

#paddle A
paddle_a=turtle.Turtle();
paddle_a.shape("square");
paddle_a.speed(0);
paddle_a.color("white");
paddle_a.penup(); # no lines
paddle_a.goto(-350,0);
paddle_a.shapesize(stretch_wid=5, stretch_len=1);

#paddle B
paddle_b=turtle.Turtle();
paddle_b.shape("square");
paddle_b.speed(0);
paddle_b.color("white");
paddle_b.penup(); # no lines
paddle_b.goto(350,0);
paddle_b.shapesize(stretch_wid=5, stretch_len=1);

#ball
ball=turtle.Turtle(); 
ball.shape("square"); 
ball.speed(0); 
ball.color("white"); 
ball.penup(); # no lines
ball.goto(0,0); 
ball.dx=0.1; ball.dy=0.1;

#pen
pen=turtle.Turtle();
pen.speed(0);
pen.color("white");
pen.hideturtle();
pen.penup();
pen.goto(0,260);
pen.write("0 - 0",align="center", font=("Courier",24, "normal"));


#functions for movement
def paddle_a_up():
    y=paddle_a.ycor();
    y+=20;
    paddle_a.sety(y);

def paddle_a_down():
    y=paddle_a.ycor();
    y-=20;
    paddle_a.sety(y);

def paddle_b_up():
    y=paddle_b.ycor();
    y+=20;
    paddle_b.sety(y);

def paddle_b_down():
    y=paddle_b.ycor();
    y-=20;
    paddle_b.sety(y);

#scores
score_a=0;
score_b=0;

#controls
wn.listen();
wn.onkeypress(paddle_a_up,"w");
wn.onkeypress(paddle_a_down,"s");
wn.onkeypress(paddle_b_up,"Up");
wn.onkeypress(paddle_b_down,"Down");

#Main loop
while(1):
    wn.update();

    #Moving the Ball
    ball.setx(ball.xcor()+ball.dx);
    ball.sety(ball.ycor()+ball.dy);

    #reflections and scoring mechanism
    if(ball.ycor()>290):
        ball.sety(290);
        ball.dy*=-1;
        playsound("audioReflection.wav")
    if(ball.ycor()<-290):
        ball.sety(-290);
        ball.dy*=-1;
        playsound("audioReflection.wav")
    if(ball.xcor()>390):
        ball.goto(0,0);
        ball.dx*=-1;
        score_a+=1;
        pen.clear(); 
        pen.write("{} - {}".format(score_a,score_b),align="center", font=("Courier",24, "normal"));
        playsound("audioGameOver.wav")

    if(ball.xcor()<-390): 
        ball.goto(0,0);
        ball.dx*=-1;
        score_b+=1;
        pen.clear(); 
        pen.write("{} - {}".format(score_a,score_b),align="center", font=("Courier",24, "normal"));
        playsound("audioGameOver.wav")

    #collisions
    if((ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40)):
        ball.setx(340);
        ball.dx*=-1;
        playsound("audioReflection.wav")
    if((ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40)):
        ball.setx(-340);
        ball.dx*=-1;
        playsound("audioReflection.wav")
