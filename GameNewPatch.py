import pygame
import random
from sys import exit

def checker(collider):
    diff = 300
    collider_last = collider.x
    collider.x = random.randrange(0, width)
    collider.y = 0
    #difference between apple spawns (min 300px difference between the last spawn)
    while collider_last + diff >= collider.x and collider_last - diff <= collider.x :
        collider.x = random.randrange(0, width)
        collider.y = 0

def getListFromImage(filePath, sizeX, sizeY):
    list = []
    index = filePath.rindex(".")
    first = filePath[:index]
    second = filePath[index:]
    for i in range(7):
        image = pygame.image.load(first + str(i) + second).convert_alpha()
        image = pygame.transform.scale(image, (sizeX,sizeY))
        list.append(image)
    return list

pygame.init()
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('AppleTreeGame')
clock = pygame.time.Clock()
font = pygame.font.Font("Pixeltype.ttf",50)
gameover_font = pygame.font.Font("Pixeltype.ttf",100)
gameover = pygame.image.load('gameover.jpg')
gameover = pygame.transform.scale(gameover, (1200,600))

score = 19
life = 3
x = 520
y = 430
vel = 7
width = 1100
height = 480

apples_vel = 3
apples_x = random.randrange(0,width)
apples_y = 0

apples = pygame.image.load("apple.png").convert_alpha()
apples = pygame.transform.scale(apples, (50,50))
apple_collider = apples.get_rect()
apple_collider2 = apples.get_rect()
apple_collider2.y = -200

dynamite = pygame.image.load("dynamite.png").convert_alpha()
dynamite = pygame.transform.scale(dynamite, (50,50))
dynamite_collider = dynamite.get_rect()
dynamite_vel = 7
dynamite_x = random.randrange(0,width)
dynamite_y = 0


background = pygame.image.load('bg.jpg')
background = pygame.transform.scale(background, (1200,600))

player_img = pygame.image.load("Goblin_idle.gif").convert_alpha()
player_img = pygame.transform.scale(player_img, (100,100))
player_collider = player_img.get_rect(topleft=(x,y))
player_index = 0

player_standing = pygame.transform.scale(pygame.image.load("Goblin_idle.gif").convert_alpha(), (100,100))
player_walking_left = getListFromImage(r"Left\left_.png",100,100)
player_walking_right = getListFromImage(r"Right\right_.png",100,100)

def init():
    global life, score, player_collider, apple_collider, apple_collider2, dynamite_collider
    life = 3
    score = 0
    player_collider = player_img.get_rect(topleft=(x,y))
    apple_collider = apples.get_rect()
    apple_collider2 = apples.get_rect()
    dynamite_collider = apples.get_rect()

def showGameOver(screen, gameover, gameover_font):
    gameover_text = gameover_font.render("Game  Over !", False, "White")
    gameover_text2 = gameover_font.render("Press SPACE to restart !", False, "White")
    screen.blit(gameover,(0,0))
    screen.blit(gameover_text, (420,150))
    screen.blit(gameover_text2, (200,270))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player_index >= len(player_walking_left): player_index = 0
        player_img = player_walking_left[int(player_index)]
        player_index += 0.15
        player_collider.left -= vel
    if keys[pygame.K_RIGHT]:
        if player_index >= len(player_walking_right): player_index = 0
        player_img = player_walking_right[int(player_index)]
        player_index += 0.15
        player_collider.right += vel

    #collisions on the edge
    if player_collider.x > width:
        player_collider.x = width
    if player_collider.x < 0:
        player_collider.x = 0

    #falling apples

    if score<10:
        apple_collider.y += apples_vel
        if apple_collider.y > height:
            checker(apple_collider)
            life -= 1

        #collision check(apples)
        if player_collider.colliderect(apple_collider):
            checker(apple_collider)
            score += 1

        life_show = font.render("Life: " + str(life), False, "Green")
        scoreboard = font.render("Score: " + str(score), False, "Green")
        screen.blit(background, (0, 0))
        screen.blit(player_img, player_collider)
        screen.blit(apples, (apple_collider.x,apple_collider.y))
        screen.blit(scoreboard, (20, 20))
        screen.blit(life_show, (20, 50))
        if life < 1:
            showGameOver(screen, gameover, gameover_font)

    if score>=10 and score<=20:
        vel = 9
        apple_collider.y += apples_vel
        apple_collider2.y += apples_vel

        if apple_collider.y > height:
            checker(apple_collider)
            life -= 1
        if apple_collider2.y > height:
            checker(apple_collider2)
            life -= 1

        #player's collision check(apples)
        if player_collider.colliderect(apple_collider):
            checker(apple_collider)
            score += 1

        if player_collider.colliderect(apple_collider2):
            checker(apple_collider2)
            score += 1

        life_show = font.render("Life: " + str(life), False, "Green")
        scoreboard = font.render("Score: " + str(score), False, "Green")
        screen.blit(background, (0, 0))
        screen.blit(player_img, player_collider)
        screen.blit(apples, (apple_collider.x,apple_collider.y))
        screen.blit(apples, (apple_collider2.x,apple_collider2.y))
        screen.blit(scoreboard, (20, 20))
        screen.blit(life_show, (20, 50))
        if life < 1:
            showGameOver(screen, gameover, gameover_font)

    if score>20:
        vel = 11
        apple_collider.y += apples_vel
        apple_collider2.y += apples_vel
        dynamite_collider.y += dynamite_vel

        if dynamite_collider.y > height:
            checker(dynamite_collider)

        if apple_collider.y > height:
            checker(apple_collider)
            life -= 1

        if apple_collider2.y > height:
            checker(apple_collider2)
            life -= 1

        #collision check(dynamite)
        if player_collider.colliderect(dynamite_collider):
            life = 0

        #collision check(apples)
        if player_collider.colliderect(apple_collider):
            checker(apple_collider)
            score += 1
            
        if player_collider.colliderect(apple_collider2):
            checker(apple_collider2)
            score += 1
        
        life_show = font.render("Life: " + str(life), False, "Green")
        scoreboard = font.render("Score: " + str(score), False, "Green")
        screen.blit(background, (0, 0))
        screen.blit(player_img, player_collider)
        screen.blit(apples, (apple_collider.x,apple_collider.y))
        screen.blit(apples, (apple_collider2.x,apple_collider2.y))
        screen.blit(dynamite, (dynamite_collider.x,dynamite_collider.y))
        screen.blit(scoreboard, (20, 20))
        screen.blit(life_show, (20, 50))
        if life < 1:
            showGameOver(screen, gameover, gameover_font)

    player_img = player_standing
    pygame.display.update()
    clock.tick(60)