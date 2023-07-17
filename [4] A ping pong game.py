# Importing turtle module
import turtle

wind = turtle.Screen()  # Creation of the Screen window
wind.title("First Project in Python by Ahmed")  # Creating a name for the Screen Window
wind.bgcolor("Black")  # Setting the Screen Background color to black
wind.setup(height=600, width=800)  # Setting the screen dimensions
wind.tracer(0)  # Stops window from updating automatically

# madrab1
madrab1 = turtle.Turtle() #Using turtle module
madrab1.speed(0)  #Making the change speed at it's maximum
madrab1.shape("square") #coding the shape of it to a square
madrab1.color("purple") #coding the color of the square to purple (player1)
madrab1.shapesize(stretch_wid= 5 , stretch_len= 1 ) #stretching the object 5 in len and not changing the width
madrab1.penup() #Making it not draw lines when it moves 
madrab1.goto(-350, 0) #Placing the start position at 350 left 0 mid
# madrab2
madrab2 = turtle.Turtle() #Importing turtle library
madrab2.speed(0) #Coding the speed of the madrab to it's maximum
madrab2.shape("square") #Making the shape a square
madrab2.color("yellow") #Making the color of player 2 yellow
madrab2.shapesize(stretch_wid= 5 , stretch_len= 1 ) #Stretching the madrab 5 in len nothing in heigh
madrab2.penup() #Making it not draw lines when it moves
madrab2.goto(350, 0) #placing the starting position of player 2 in the right and 0 mid
# ball
ball = turtle.Turtle() #Importing turtle module
ball.speed(0) #Making the speed of the object at it's maximum
ball.shape("square") #Setting the shape of the mid object to a square as there is no ball shape
ball.color("white") #Making the mid object color to white
ball.penup() #Coding the object to not draw lines/pen up when it moves
ball.goto(0, 0) #Set the statting position to 0 0
ball.dx = 2 #Make the ball X coordinates increase by 0.2
ball.dy = 2 #Make the ball Y coordinates increase by 0.2

#Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed = 0
score.color("white")
score.penup()
score.hideturtle()
score.goto(0 , 260)
score.write("Player 1: 0 Player 2 : 0", align="center", font=("Arial", 24, "normal"))

#Functions
def madrab1_up():   #Function of the first object going upwards
    y = madrab1.ycor()  #Gets the Y coordinates of the first object
    y += 20    #Adds 20 pixels on the coordinates
    madrab1.sety(y)   #Setting the current coordinates to the added ones

def madrab1_down():  #Function of the first object going downwards
    y = madrab1.ycor()  #Gets the Y coordinates of the first object 
    y -= 20  #Subtarcts 20 pixels on the coords which makes it go downards
    madrab1.sety(y) #Setting the current coordinates to the subtracted ones

def madrab2_up(): #Function of the second object going upwards
    y = madrab2.ycor() #Gets the Y coordinates of the second object
    y += 20 #Adds 20 pixels on the coordinates
    madrab2.sety(y) #Setting the current coordinates to the added ones

def madrab2_down(): #Function of the second object going downards
    y = madrab2.ycor() #Gets the Y coordinates of the second object 
    y -= 20 #Subtacts 20 pixels on the coordinates
    madrab2.sety(y) #Setting the current coordinates to the subtracted ones
#Key Bindings
wind.listen() #Making the window screen expect/listen for any key inputs
wind.onkeypress(madrab1_up , "w") #on w keypress object1 moves upwards
wind.onkeypress(madrab1_down , "s") 
wind.onkeypress(madrab2_up , "Up") 
wind.onkeypress(madrab2_down , "Down") 

# main game loop
while True:
    wind.update()  # Updates the screen when the loop runs

    #Moving the ball
    ball.setx(ball.xcor() + ball.dx) #Setting the X coordinates to = current + 0.2
    ball.sety(ball.ycor() + ball.dy) #Setting the Y coordinates to = current + 0.2

    #Coding Borders for the ball Top border:300 , Bottom border:-300, ball is 20 px,  10 up 10 down
    if ball.ycor() >290: #If Y coordinates more than 290 
        ball.sety(290) #Make it go ti 290 coords
        ball.dy *= -1 #Make it decrease by -1/opposite direction
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() >390: #If ball is at Right border Right:400, Left:-400 , Ball:20pxUp , 20pxDown
        ball.goto(0 , 0) #set it to go to 0 , 0
        ball.dx *= -1 #make the ball go in the opposite direction
        score1 += 1 
        score.clear()
        score.write("Player 1: {} Player 2 : {}".format(score1, score2), align="center", font=("Arial", 24, "normal"))
    if ball.xcor() <-390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score2 += 1 
        score.clear()
        score.write("Player 1: {} Player 2 : {}".format(score1, score2), align="center", font=("Arial", 24, "normal"))

    #Collision Between the madrab and ball
    if (ball.xcor() > 340 and ball.xcor() <350 and ball.ycor() <madrab2.ycor() +40 and ball.ycor() >madrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() >-350 and ball.ycor() <madrab1.ycor() +40 and ball.ycor() >madrab1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1