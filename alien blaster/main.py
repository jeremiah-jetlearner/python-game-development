import pgzrun
from random import randint

WIDTH=500
HEIGHT=500

score=0
message=""

alien=Actor("alien")
alien.x=randint(0,450)
alien.y=randint(0,450)

def draw():
    screen.fill("yellow")
    alien.draw()
    screen.draw.text(message,center=(400,10),fontsize=30)
    screen.draw.text("Score:"+str(score),center=(50,50),fontsize=30)

def update():
    pass

def on_mouse_down(pos):
    global message,score
    if alien.collidepoint(pos):
        alien.x=randint(0,450)
        alien.y=randint(0,450)
        message="GOOD SHOT"
        score+=10
    else:
        message="YOU MISSED"


    
pgzrun.go()

    

