import pgzrun
import random

WIDTH= 700
HEIGHT= 600

bow= Actor("bow.png")

bow.dead= False
bow.countdown= 90
bow.pos= (WIDTH//2, HEIGHT- 60)
speed= 5
target= []
arrows= []
score= 0
direction= 1

for e in range(8):
    for q in range(4):
        op= Actor("target.png")
        target.append(op)
        target[-1].x = 100+ 50* e
        target[-1].y = 100+ 50* q

def draw():
    screen.clear()
    screen.fill("royal blue")
    if not bow.dead:
        bow.draw()
    screen.draw.text("Score = "+ str(score), (50,50))
    for t in target:
        t.draw()
    for a in arrows:
        a.draw()
    if len(target)== 0 or bow.dead:
        screen.clear() 
        game_over()
    print(bow.dead)
            

def game_over():
    screen.draw.text("Game Over", (WIDTH/ 2, HEIGHT/ 2) )

def update():
    global score, direction, arrows
    if keyboard.left:
        bow.x -= speed
        if bow.x <= 40:
            bow.x= 40
    elif keyboard.right:
        bow.x += speed
        if bow.x >= WIDTH- 40:
            bow.x= WIDTH - 40
    for a in arrows:
        if a.y <= 0:
            arrows.remove(a)
        else:
            a.y-= 10
    if len(target)> 0 and (target[-1].x > WIDTH- 80 or target[0].x < 80):
        direction= direction *-1
    for t in target:
        t.y += 0.5
        t.x += 5* direction
        if t.y >= HEIGHT:
            target.remove(t)
            '''e.y= -100
            e.x = random.randint(40, WIDTH- 40)'''
        for a in arrows:
            if t.colliderect(a):
                '''sounds.eep.play()'''
                score+= 100 
                arrows.remove(a)
                target.remove(t)
                if len(target)== 0:
                    game_over()
        if t.colliderect(bow):
            bow.dead= True
    if bow.dead:
        bow.countdown-= 1
    '''if ship.countdown== 0:
        ship.dead= False
        ship.countdown= 90'''
 
def on_key_down(key):
    global arrows 
    if bow.dead == False: # !ship.dead
        if key == keys.SPACE:
            arrows.append(Actor("arrow.png"))
            arrows[-1].x= bow.x
            arrows[-1].y= bow.y- 50

pgzrun.go()