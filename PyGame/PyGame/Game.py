import pygame
import random
import time
from sys import exit
pygame.init()

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('AppleTreeGame')
clock = pygame.time.Clock()
font = pygame.font.Font("Pixeltype.ttf",50)

score = 0
x = 520
y = 430
vel = 7
width = 1100
height = 600

apples_vel = 3
apples_x = random.randrange(0,width)
apples_y = 0
apples = pygame.image.load("apple.png").convert_alpha()
apples = pygame.transform.scale(apples, (50,50))
apple_collider = apples.get_rect()


background = pygame.image.load('bg.jpg')

player_img = pygame.image.load("Goblin_idle.gif").convert_alpha()
player_img = pygame.transform.scale(player_img, (100,100))
player_rect = player_img.get_rect(topleft=(x,y))

player_walking_left0 = pygame.image.load(r"Left\left_0.jpg")
player_walking_left0 = pygame.transform.scale(player_walking_left0, (100,100))
player_walking_left1 = pygame.image.load(r"Left\left_1.jpg")
player_walking_left1 = pygame.transform.scale(player_walking_left1, (100,100))
player_walking_left2 = pygame.image.load(r"Left\left_2.jpg")
player_walking_left2 = pygame.transform.scale(player_walking_left2, (100,100))
player_walking_left3 = pygame.image.load(r"Left\left_3.jpg")
player_walking_left3 = pygame.transform.scale(player_walking_left3, (100,100))
player_walking_left4 = pygame.image.load(r"Left\left_4.jpg")
player_walking_left4 = pygame.transform.scale(player_walking_left4, (100,100))
player_walking_left5 = pygame.image.load(r"Left\left_5.jpg")
player_walking_left5 = pygame.transform.scale(player_walking_left5, (100,100))
player_walking_left6 = pygame.image.load(r"Left\left_6.jpg")
player_walking_left6 = pygame.transform.scale(player_walking_left6, (100,100))
player_walking_left7 = pygame.image.load(r"Left\left_7.jpg")
player_walking_left7 = pygame.transform.scale(player_walking_left7, (100,100))
player_walking_left = [player_walking_left0,player_walking_left1,player_walking_left3,player_walking_left4,player_walking_left5,player_walking_left6,player_walking_left7]
player_index = 0
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
        player_index += 0.10
        player_rect.left -= vel
    if keys[pygame.K_RIGHT]:
        player_img = pygame.image.load("Goblin_run_right.gif").convert_alpha()
        player_img = pygame.transform.scale(player_img, (100,100))
        player_rect.right += vel
    

    #collisions on the edge
    if player_rect.x > width:
       player_rect.x = width
    if player_rect.x < 0:
       player_rect.x = 0
        #falling apples
    apple_collider.y += apples_vel
    if apple_collider.y > height:
        apple_collider_last = apple_collider.x
        apple_collider.x = random.randrange(0, width)
        apple_collider.y = 0
        diff = 300
        #difference between apple spawns (min 300px difference between the last spawn)
        while apple_collider_last + diff >= apple_collider.x and apple_collider_last - diff <= apple_collider.x :
            apple_collider.x = random.randrange(0, width)
            apple_collider.y = 0

    #collision check(apples)
    if player_rect.colliderect(apple_collider):
        score += 1
        apple_collider_last = apple_collider.x
        apple_collider.x = random.randrange(0, width)
        apple_collider.y = 0
        diff = 300
        #difference between apple spawns (min 300px difference between the last spawn)
        while apple_collider_last + diff >= apple_collider.x and apple_collider_last - diff <= apple_collider.x :
            apple_collider.x = random.randrange(0, width)
            apple_collider.y = 0
    scoreboard = font.render("Score: " + str(score), False, "Green")
    screen.blit(background, (0, 0))
    screen.blit(player_img, player_rect)
    screen.blit(apples, (apple_collider.x,apple_collider.y))
    screen.blit(scoreboard, (20, 20))
    player_img = pygame.image.load("Goblin_idle.gif").convert_alpha()
    player_img = pygame.transform.scale(player_img, (100,100))
    pygame.display.update()
    clock.tick(60)