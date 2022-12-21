from dis import dis
import py
import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800,600))

background = pygame.image.load(open(r'C:\Users\HP\.vscode\all_langauage_programe_file\only python file\Python project\space_invanders_game\5586938.jpg'))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(open(r'C:\Users\HP\.vscode\all_langauage_programe_file\only python file\Python project\space_invanders_game\spaceship.png'))
pygame.display.set_icon(icon)


playerImg = pygame.image.load(open(r"C:\Users\HP\.vscode\all_langauage_programe_file\only python file\Python project\space_invanders_game\arcade-game.png"))
playerx = 370
playery = 480
playerx_change = 0

## enemy
enemyImg = []
enemyX = []
enemyY = []
enemyx_change = []
enemyy_change = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load(open(r"C:\Users\HP\.vscode\all_langauage_programe_file\only python file\Python project\space_invanders_game\main.py")))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyx_change.append(0.15)
    enemyy_change.append(40)

bulletImg = pygame.image.load(open(r"C:\Users\HP\.vscode\all_langauage_programe_file\only python file\Python project\space_invanders_game\bullet.png"))
bulletX = 0
bulletY = 480
bulletx_change = 0
bullety_change = 1.50
bullet_state = "ready"

score = 0
font = pygame.font.Font('freesansbold.ttf',25)
textx = 10
texty = 10


over_font = pygame.font.Font('freesansbold.ttf',64)


def show_score(x,y):
    scores = font.render("score: "+str(score),True,(255,255,255))
    screen.blit(scores,(x,y))

def game_over_text():
    game_over = over_font.render("Game is over",True,(255,255,255))
    screen.blit(game_over,(200,250))

def player(x,y):
    screen.blit(playerImg,(x,y))


def enmy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

def iscollision(enemX,enemY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemX-bulletX,2)) + (math.pow(enemY-bulletY,2)))
    if distance<27:
        return True
    else:
        return False    

running = True
while running:

    screen.fill((0,0,0))  
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.6
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.6    
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerx
                    fire_bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    # boundry for spece ship
    playerx += playerx_change

    if playerx <=0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736    

    # boundry for enmy 
    for i in range(num_of_enemy):

        if enemyY[i] > 440:
            for j in range(num_of_enemy):
                enemyY[j] = 2000
            game_over_text()
            break    

        enemyX[i] += enemyx_change[i]
        if enemyX[i] <=0:
            enemyx_change[i] = 0.4
            enemyY[i] += enemyy_change[i]
        elif enemyX[i] >= 736:
            enemyx_change[i] = -0.4 
            enemyY[i] += enemyy_change[i]

        collision = iscollision(enemyX[i],enemyY[i],bulletX,bulletY)

        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50,150)    

        enmy(enemyX[i],enemyY[i],i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"


    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bullety_change

    

    

    player(playerx,playery)   
    show_score(textx,texty)  
    pygame.display.update()