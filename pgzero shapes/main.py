import pgzrun
from random import randint

WIDTH=300
HEIGHT=300

def draw():
    swidth=WIDTH
    sheight=HEIGHT-200
    for i in range(20):
        square=Rect(0,0,swidth,sheight)
        square.center=(150,150)
        screen.draw.rect(square,'blue')
        swidth-=10
        sheight+=10


def update():
    pass

pgzrun.go()
