from this import s
import pygame
import random
from sys import exit
pygame.init()

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('AppleTreeGame')
clock = pygame.time.Clock()
font = pygame.font.Font("Pixeltype.ttf",50)
game_state = "active"

score = 0
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

dynamite = pygame.image.load("dynamite.png").convert_alpha()
dynamite = pygame.transform.scale(dynamite, (50,50))
dynamite_collider = dynamite.get_rect()
dynamite_vel = 7
dynamite_x = random.randrange(0,width)
dynamite_y = 0


background = pygame.image.load('bg.jpg')

player_img = pygame.image.load("Goblin_idle.gif").convert_alpha()
player_img = pygame.transform.scale(player_img, (100,100))
player_rect = player_img.get_rect(topleft=(x,y))
player_index = 0

player_walking_left0 = pygame.image.load(r"Left\left_0.png").convert_alpha()
player_walking_left0 = pygame.transform.scale(player_walking_left0, (100,100))
player_walking_left1 = pygame.image.load(r"Left\left_1.png").convert_alpha()
player_walking_left1 = pygame.transform.scale(player_walking_left1, (100,100))
player_walking_left2 = pygame.image.load(r"Left\left_2.png").convert_alpha()
player_walking_left2 = pygame.transform.scale(player_walking_left2, (100,100))
player_walking_left3 = pygame.image.load(r"Left\left_3.png").convert_alpha()
player_walking_left3 = pygame.transform.scale(player_walking_left3, (100,100))
player_walking_left4 = pygame.image.load(r"Left\left_4.png").convert_alpha()
player_walking_left4 = pygame.transform.scale(player_walking_left4, (100,100))
player_walking_left5 = pygame.image.load(r"Left\left_5.png").convert_alpha()
player_walking_left5 = pygame.transform.scale(player_walking_left5, (100,100))
player_walking_left6 = pygame.image.load(r"Left\left_6.png").convert_alpha()
player_walking_left6 = pygame.transform.scale(player_walking_left6, (100,100))
player_walking_left7 = pygame.image.load(r"Left\left_7.png").convert_alpha()
player_walking_left7 = pygame.transform.scale(player_walking_left7, (100,100))
player_walking_left = [player_walking_left0,player_walking_left1,player_walking_left3,player_walking_left4,player_walking_left5,player_walking_left6,player_walking_left7]

player_walking_right0 = pygame.image.load(r"Right\right_0.png").convert_alpha()
player_walking_right0 = pygame.transform.scale(player_walking_right0, (100,100))
player_walking_right1 = pygame.image.load(r"Right\right_1.png").convert_alpha()
player_walking_right1 = pygame.transform.scale(player_walking_right1, (100,100))
player_walking_right2 = pygame.image.load(r"Right\right_2.png").convert_alpha()
player_walking_right2 = pygame.transform.scale(player_walking_right2, (100,100))
player_walking_right3 = pygame.image.load(r"Right\right_3.png").convert_alpha()
player_walking_right3 = pygame.transform.scale(player_walking_right3, (100,100))
player_walking_right4 = pygame.image.load(r"Right\right_4.png").convert_alpha()
player_walking_right4 = pygame.transform.scale(player_walking_right4, (100,100))
player_walking_right5 = pygame.image.load(r"Right\right_5.png").convert_alpha()
player_walking_right5 = pygame.transform.scale(player_walking_right5, (100,100))
player_walking_right6 = pygame.image.load(r"Right\right_6.png").convert_alpha()
player_walking_right6 = pygame.transform.scale(player_walking_right6, (100,100))
player_walking_right7 = pygame.image.load(r"Right\right_7.png").convert_alpha()
player_walking_right7 = pygame.transform.scale(player_walking_right7, (100,100))
player_walking_right = [player_walking_right0,player_walking_right1,player_walking_right3,player_walking_right4,player_walking_right5,player_walking_right6,player_walking_right7]

def checker(obj_type):
    if obj_type == "apple":
        apple_collider_last = apple_collider.x
        apple_collider.x = random.randrange(0, width)
        apple_collider.y = 0
        diff = 300
        #difference between apple spawns (min 300px difference between the last spawn)
        while apple_collider_last + diff >= apple_collider.x and apple_collider_last - diff <= apple_collider.x :
            apple_collider.x = random.randrange(0, width)
            apple_collider.y = 0

    if obj_type == "apple2":
        apple_collider2_last = apple_collider2.x
        apple_collider2.x = random.randrange(0, width)
        apple_collider2.y = 0
        diff = 300
        #difference between apple spawns (min 300px difference between the last spawn)
        while apple_collider2_last + diff >= apple_collider2.x and apple_collider2_last - diff <= apple_collider2.x:
            apple_collider2.x = random.randrange(0, width)
            apple_collider2.y = 0

    if obj_type == "dynamite":
        dynamite_collider_last = apple_collider.x
        dynamite_collider.x = random.randrange(0, width)
        while dynamite_collider_last + diff >= dynamite_collider.x and dynamite_collider_last - diff <= dynamite_collider.x:
            dynamite_collider.x = random.randrange(0, width)
            dynamite_collider.y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()

    if game_state == "over" or score < 0:
        background = pygame.image.load('gameover.jpg')
        background = pygame.transform.scale(background, (1200,600))

    if game_state == "active": 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if player_index >= len(player_walking_left): player_index = 0
            player_img = player_walking_left[int(player_index)]
            player_index += 0.10
            player_rect.left -= vel
        if keys[pygame.K_RIGHT]:
            if player_index >= len(player_walking_right): player_index = 0
            player_img = player_walking_right[int(player_index)]
            player_index += 0.10
            player_rect.right += vel
        

        #collisions on the edge
        if player_rect.x > width:
            player_rect.x = width
        if player_rect.x < 0:
            player_rect.x = 0

        #falling apples
        if score<10:
            apple_collider.y += apples_vel
            if apple_collider.y > height:
                checker("apple")
                score -= 1

            #collision check(apples)
            if player_rect.colliderect(apple_collider):
                checker("apple")
                score += 1

            scoreboard = font.render("Score: " + str(score), False, "Green")
            screen.blit(background, (0, 0))
            screen.blit(player_img, player_rect)
            screen.blit(apples, (apple_collider.x,apple_collider.y))
            screen.blit(scoreboard, (20, 20))

        if score>=10 and score<=20:
            vel = 9
            apple_collider.y += apples_vel
            apple_collider2.y += apples_vel

            if apple_collider.y > height:
                checker("apple")
                score -= 1
            if apple_collider2.y > height:
                checker("apple2")
                score -= 1

            #player's collision check(apples)
            if player_rect.colliderect(apple_collider):
                checker("apple")
                score += 1

            if player_rect.colliderect(apple_collider2):
                checker("apple2")
                score += 1

            scoreboard = font.render("Score: " + str(score), False, "Green")
            screen.blit(background, (0, 0))
            screen.blit(player_img, player_rect)
            screen.blit(apples, (apple_collider.x,apple_collider.y))
            screen.blit(apples, (apple_collider2.x,apple_collider2.y))
            screen.blit(scoreboard, (20, 20))
            scoreboard = font.render("Score: " + str(score), False, "Green")

        if score>20:
            vel = 11
            apple_collider.y += apples_vel
            apple_collider2.y += apples_vel
            dynamite_collider.y += dynamite_vel
            if dynamite_collider.y > height:
               checker("dynamite")

            if apple_collider.y > height:
                checker("apple")
                score -= 1

            if apple_collider2.y > height:
                checker("apple2")
                score -= 1

            #collision check(dynamite)
            if player_rect.colliderect(dynamite_collider):
                checker("dynamite")
                game_state = "over"

            #collision check(apples)
            if player_rect.colliderect(apple_collider):
                checker("apple")
                score += 1
            
            if player_rect.colliderect(apple_collider2):
                checker("apple2")
                score += 1

            scoreboard = font.render("Score: " + str(score), False, "Green")
            screen.blit(background, (0, 0))
            screen.blit(player_img, player_rect)
            screen.blit(apples, (apple_collider.x,apple_collider.y))
            screen.blit(apples, (apple_collider2.x,apple_collider2.y))
            screen.blit(dynamite, (dynamite_collider.x,dynamite_collider.y))
            screen.blit(scoreboard, (20, 20))
            scoreboard = font.render("Score: " + str(score), False, "Green")

    player_img = pygame.image.load("Goblin_idle.gif").convert_alpha()
    player_img = pygame.transform.scale(player_img, (100,100))
    pygame.display.update()
    clock.tick(60)