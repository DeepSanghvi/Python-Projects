#Snake game created by Deep Sanghvi

import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0

# the Background acreen settings
wn = turtle.Screen()
wn.title("Snake_Game")
wn.bgcolor("antiquewhite4")
wn.setup(width = 600, height = 600)
wn.tracer(0)


# the snake head settings
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("Brown1")
head.penup()
head.goto(100,100)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("darkgoldenrod")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 20, "bold"))



#Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def stop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 15)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 15)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 15)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 15)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(stop, "s")

#Main game loop
while True:

    wn.update()

    #check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(delay*10)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        # clear the segments list
        segments.clear()

        # Reset the delay
        delay = 0.1

        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "bold"))


    #check for the collision with the food
    if head.distance(food) < 20:
        #move the food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # Add a snake body segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("pink")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay to increase the game speed to make complicated
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "bold"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # check for head collision with the body segments

    time.sleep(delay)

wn.mainloop()
