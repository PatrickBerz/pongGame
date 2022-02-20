# program Name: Pong
# Desc: plays pong
# Author: prberzins@guerincatholic.org
# Date: 9/24/18

from tkinter import *
import random
# Initialize variables and constants for the program
dx, dy = 15, 15                # change in x y positions
canvWidth, canvHeight = 800, 400      # graphics screen window height and width
ballSize = 25             # diameter of the ball
rackBrd, rackWidth, rackHeight, rackSp2 = 40, 15, 90, 30  # racquet parameters
rackSp = 30
lplayer=rplayer=0



def lup(event):                 # method to move left racquet up, called by "w" enter
    global lpos, rackSp2         # make variables defined outside of method global for use
    if lpos > 0:  # only move up if room left
        if lpos - rackSp2 < 0:       # if less than rack speed, then set to 0
            lpos = 0
        else:
            lpos -= rackSp2          # move up rackspeed distance

def rup(event):                 # method to move left racquet up, called by "o" enter
    global rpos, rackSp         # make variables defined outside of method global for use
    if rpos > 0:  # only move up if room left
        if rpos - rackSp < 0:       # if less than rack speed, then set to 0
            rpos = 0
        else:
            rpos -= rackSp

def ldown(event):               # method to move left racquet down, called by "s" enter
    global lpos, rackSp2, canvHeight # make variables defined outside of method global for use
    if lpos > (canvHeight-rackHeight):# only move down if room left
        if lpos - rackSp > 400:
            lpos = canvHeight-rackHeight
    else:
        lpos += rackSp2

def rdown(event):               # method to move right racquet down, called by "l" enter
    global rpos, rackSp, canvHeight, rackHeight # make variables defined outside of method global for use
    if rpos > (canvHeight-rackHeight):# only move down if room left
        if rpos - rackSp > 400:
            rpos = canvHeight-rackHeight
    else:
        rpos += rackSp

def rmove(event):
    global rpos, canvHeight,rackHeight
    ypos = event.y
    if ypos > 0 and ypos < (canvHeight-rackHeight): # if in range
        rpos = ypos

def cheat(event): #(cheat)press P to freeze player1 paddle in place
    global rackSp2
    rackSp2 = 0

def uncheat(event): #press o to unfreeze player1 paddle
    global rackSp2
    rackSp2 = 30

def ballshrink(event):      #shrinks ball to 1 pixel with ; key
    global ballSize
    ballSize = 1

def ballnormal(event):     #puts ball back to normal with L jey
    global ballSize
    ballSize = 25

def move():                     # method to move all objects, updates ball position
    global x1, y1, dx, dy, playing, canvWidth, canvHeight, ballSize, rackBrd
    global lplayer, rplayer, nextplayer, counter, lpos, rpos, rackBrd
    if playing > 0:
        x1 += dx
        y1 += dy
    else:
        if nextplayer == 0:
            x1 = rackBrd-10
            y1 = lpos+(rackHeight-ballSize)/2
            dx = abs(dx)
        else:
            x1 = canvWidth-rackBrd-10
            y1 = rpos+(rackHeight-ballSize)/2
            dx = -abs(dx)
    if y1 > canvHeight-ballSize:
        y1 = canvHeight-ballSize
        dy = -dy
    if y1 < 0:
        y1 = 0
        dy = -dy
    if x1 > (canvWidth-ballSize):
        lplayer=lplayer+1   #adds score to player 1
        if lplayer == 5:
            can.create_text(canvWidth/2,canvHeight/2, text="Player1 WINS!", font=font2, fill="yellow")
            screen.mainloop(quit(mainloop()))              #prints out who won and freezes screen
        x1 = rackBrd
        y1 = (canvHeight / 2)
        nextplayer = 0
        playing = 0
    if x1 < 0:
        rplayer=rplayer+1      #adds score to player 2
        if rplayer == 5:
            can.create_text(canvWidth/2,canvHeight/2, text="Player2 WINS!", font=font2, fill="yellow")
            screen.mainloop(quit(mainloop()))      #prints out who won and freezes screen
        x1 = canvWidth-rackBrd
        y1 = (canvHeight/2)
        nextplayer = 1
        playing = 0
    if x1 <= rackBrd:
        if y1 > lpos - ballSize and y1 < (lpos+rackHeight):#tells the ball to bounce off of the paddle when it collides
            x1 = rackBrd+5
            dx = 14     #sets the speed it comes off at
            if y1>lpos + (rackHeight*6/8) and y1 < lpos+(rackHeight):  # sets spots on paddle that ball will pounce off
                dx = 30                                                # faster
            if y1 > lpos - ballSize and y1 < lpos + (rackHeight/8):
                dx = 30

    if x1 >= (canvWidth - rackBrd-ballSize):
        if y1 >= rpos - ballSize and y1 <= (rpos+rackHeight):  #tells the ball to bounce off of the paddle when it collides
            x1 = (canvWidth-rackBrd-ballSize-5)
            dx = -14
        if y1 > rpos + (rackHeight*6/8) and y1 < rpos+(rackHeight): # sets spots on paddle that ball will pounce off
            dx = - 30                                               # faster
        if y1 > rpos -ballSize and y1 < rpos + (rackHeight/8):
            dx = -30

    # after ball x y updated draw new ball on screen
    can.coords(oval1, x1, y1, x1 + ballSize, y1 + ballSize)
    score = str(lplayer) + ":" + str(rplayer)  #puts score on screen
    can.itemconfigure(counter, text=score)
    # Change the position of the rackets
    can.coords(lracket, rackBrd, lpos, rackBrd, lpos+rackHeight)
    can.coords(rracket, canvWidth-rackBrd, rpos, canvWidth-rackBrd, rpos+rackHeight)
    screen.after(55, move)   # update ball position after delay



def start(event):
   global playing
   playing = 1

# main program for game, first initialize ball and racquet location variables

x1, y1 = rackBrd, (canvHeight-ballSize)/2
rpos = lpos = (canvHeight-rackWidth)/2
nextplayer = 0
playing = 0

# initialize tk window, set title, paint the Canvas
screen = Tk()
screen.title("Pong")
can=Canvas(screen, bg='blue',height=canvHeight, width = canvWidth)
can.pack(side="left")# pack main canvas
goal = can.create_line(765, 0, 765, 400, width=2.5, dash=(10,8))
goal2 = can.create_line(35, 0, 35, 400, width=2.5, dash=(10,8))
# Draw the midcourt line
line = can.create_line(canvWidth/2,0,canvWidth/2,canvHeight, width =3.5, fill="black", dash=(7,15))
circle = can.create_oval(365,165, 435, 235, width=3.5, dash=(4, 15), fill="blue")
# Draw the ball
oval1 = can.create_oval(x1, y1, x1 + ballSize, y1 + ballSize, width=2, fill="white")
# Draw the paddle
lracket = can.create_line(rackBrd, lpos, rackBrd, lpos+rackHeight, width=rackWidth, fill="orange")
rracket = can.create_line(rackWidth, rpos, rackWidth-rackBrd, rpos+rackHeight, width=rackWidth, fill="orange")
font=('courier',25)
counter = can.create_text(canvWidth/2, 20, text="0:0", font=font, fill="white")
font2=("arial", 50)


# Use the keyboard inputs to move the rackets
screen.bind('w',lup)       # bind the w key to call the lup method, it updates location
screen.bind('s',ldown) # bind the s key to call the ldown method, it updates location
screen.bind("i", rup) #bind the i key with rup
screen.bind("k", rdown) #bind the k key with rdown
screen.bind("p", cheat)  #bind p to cheat
screen.bind("o", uncheat)  #bind o to uncheat
screen.bind("<space>", start)  #bind space to start to serve the ball
screen.bind('<B1-Motion>', rmove)
screen.bind(";", ballshrink)
screen.bind("l", ballnormal)

move()                  # call the move method to update the ball position
screen.mainloop()


