# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 12:53:12 2022
@author: anast
"""

# notation: single # is for certain, double # is for uncertain

from random import randrange
#This line imports a random element from a range that we can specify
from turtle import *
#imports a symbol from the turtle graphics library
import turtle as turd
#imports the module Turtle

from freegames import square, vector
#imports a position vector used as reference for objects
import sys
import os



food = vector(0, 0)
#position of the food
snake = [vector(10, 0)]
#position of the snake
aim = vector(0, -10)
## where the snake is heading
wall = vector(420,420)
walls = [wall]
l = 1



def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y
#this allows for a change in direction of the snake


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190
#makes sure that you can't go out of bounds


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)
#allows the snake to move
    
    if not inside(head) or head in snake or head in walls:
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
        
        
        return
#if you run into yourself or the boundary, this makes the tile you run into red
    snake.append(head)
##updates the system on the position of the head
    if head == food:
#detects if the head is inside the food
        
        
        print('Snake:', len(snake))
## increases the length of the snake
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
#generates a new position for the food
        
        l = len(snake) - 1
    
        # for l in range(len(snake)):
        
        tempwallx = randrange(-15, 15) * 10
        tempwally = randrange(-15, 15) * 10 
        walls.append(vector(tempwallx,tempwally))
            
    else:
        snake.pop(0)
    clear()
#this makes the snake update to keep a consistent length, honestly its pretty fun to try and play without this,
    #maybe a good idea for someone else
    for body in snake:
        square(body.x, body.y, 9, 'purple')
#codes to make the body of the snake black, as well as the size of the cube
#petition for our group to make this purple because that would be fun, we could do this by changing 'black' to 'purple'
    square(food.x, food.y, 9, 'green')
#this makes the food green, as well as setting its dimensions
    for i in range(len(walls)):
        square(walls[i].x, walls[i].y, 9, 'black')
    # square(wall.x, wall.y, 9, 'black')
    update()
    ontimer(move, 100)
#sets speed, possibility for difficulty settings by changing this

setup(414, 414, 369, 0)
#sets up the size of the play area, perhaps putting on a visable border would be good as currently the border is white
hideturtle()
#this removes a little arrow thing that shows the last item that turtle puts in
tracer(False)
#this makes the items just appear quickly instead of being traced in one line at a time
listen()
##seems to literally be the thing that makes the system "listen" to the player's commands

onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
#these collectively define the speeds for the snake
move()
       
## no idea what this does but if its not there, the game doesn't load
done()
#this allows the game to update (eg. move), as well as making the close button work, (I learned that the hard way)
#overall notes: 
#if we could figure out how to not have to repaste the code after exiting that would be good
    #this seems to be a problem with the "setup(420, 420, 370, 0)" line but i'm not sure why
