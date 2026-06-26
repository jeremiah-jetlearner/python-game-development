import pgzrun
from random import randint

WIDTH=500
HEIGHT=500

score=0

bee=Actor("bumble bee")
bee.x=randint(0,450)
bee.y=randint(0,450)
flower=Actor("flower")
flower.x=300
flower.y=200

def draw():
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
    
def update():
    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
        bee.y=bee.y+2
    if bee.colliderect(flower):
        flower.x=randint(0,450)
        flower.y=randint(0,450)

pgzrun.go()
    
