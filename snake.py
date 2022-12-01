#Anastasia Kimovska: AK
#Quinn Myers: QM
#Tesse Klompstra: TK

#Original comments about the pre-existing code done by QM

# notation: single # is for certain, double # is for uncertain-QM
"""Snake, classic arcade game.
Exercises
1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
#This line imports a random element from a range that we can specify-QM
from turtle import *
#imports a symbol from the turtle graphics library-QM
import turtle as turd
#imports the module Turtle-AK

from freegames import square, vector
#imports a position vector used as reference for objects-QM
import sys
import os
#imported to restart the game-AK


food = vector(0, 0)
#position of the food-QM
snake = [vector(10, 0)]
#position of the snake-QM
aim = vector(0, -10)
## where the snake is heading-QM


wall = vector(420,420) 
walls = [wall]
#creating a list of walls to be able to give wall positions different vectors- TK



def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y
#this allows for a change in direction of the snake-QM


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190
#makes sure that you can't go out of bounds-QM


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)
#allows the snake to move-QM
    
    if not inside(head) or head in snake or head in walls:
        #added 'head in walls' to ensure hitting the walls causes the snake game to end- AK
        square(head.x, head.y, 9, 'red')
        update()
        
        while True:
            update()
            answer = input('do you want to restart Y/N?')
            if answer == "N":
                print ("Leaving the game")
                sys.exit(0) # import sys module 
            elif answer == "Y":
                print ("Starting new game")
                python = sys.executable
                os.execl(python, python, * sys.argv)
#while loop to allow the user to restart the game without having to clear the tab and reboot on the powershell every
#time the user wants to play- AK
        
        
        return
#if you run into yourself or the boundary, this makes the tile you run into red-QM
    snake.append(head)
##updates the system on the position of the head-QM
    if head == food:
#detects if the head is inside the food-QM
        
        
        print('Snake:', len(snake))
## increases the length of the snake-QM
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
#generates a new position for the food-QM
        
        tempwallx = randrange(-15, 15) * 10
        tempwally = randrange(-15, 15) * 10 
        walls.append(vector(tempwallx,tempwally))
#giving the wall a random vector, and appending it to the list mentioned previously above- TK
            
    else:
        snake.pop(0)
            
    clear()
#this makes the snake update to keep a consistent length-QM
    for body in snake:
        square(body.x, body.y, 9, 'purple')
#codes to make the body of the snake black, as well as the size of the cube-QM
    square(food.x, food.y, 9, 'green')
#this makes the food green, as well as setting its dimensions-QM
    for i in range(len(walls)):
        square(walls[i].x, walls[i].y, 9, 'black')
#makes the walls. made them black and the same dimensions as the food and snake-AK

        if food.x == walls[i].x and food.y == walls[i].y:
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
    #ensures that the generated food and walls do not end up on the same vector-AK
     
    update()
    ontimer(move, 100)
#sets speed, possibility for difficulty settings by changing this-QM

setup(414, 414, 369, 0)
#sets up the size of the play area, perhaps putting on a visable border would be good as currently the border is white-QM
hideturtle()
#this removes a little arrow thing that shows the last item that turtle puts in-QM
tracer(False)
#this makes the items just appear quickly instead of being traced in one line at a time-QM
listen()
##seems to literally be the thing that makes the system "listen" to the player's commands-QM

onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
#these collectively define the speeds for the snake-QM
move()       
## no idea what this does but if its not there, the game doesn't load
done()
#this allows the game to update (eg. move), as well as making the close button work
#overall notes: 
#if we could figure out how to not have to repaste the code after exiting that would be good
    #this seems to be a problem with the "setup(420, 420, 370, 0)"