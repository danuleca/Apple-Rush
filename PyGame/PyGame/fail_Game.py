import pygame
import random
import time
from sys import exit

class apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.apples_vel = 3
        self.apples_x = random.randrange(0,width)
        self.apples_y = 0
        self.apples_img = pygame.image.load("apple.png").convert_alpha()
        self.apples_img = pygame.transform.scale(self.apples_img, (50,50))
        self.apple_collider = self.apples_img.get_rect()

    def falling_apples(self):
        self.apple_collider.y += self.apples_vel
        if self.apple_collider.y > 500:
            self.apple_collider.x = random.randrange(0, width)

            #difference between apple spawns (min 300px difference between the last spawn)
            while self.apple_collider_last + 300 >= self.apple_collider.x and self.apple_collider_last - 300 <= self.apple_collider.x :
                self.apple_collider.x = random.randrange(0, width)
            self.apple_collider.y = 0
    
    def collision_check(self):
        if self.player_rect.colliderect(self.apple_collider):
            apple_collider_last = self.apple_collider.x
            diff = 300
            self.apple_collider.x = random.randrange(0, width)
            #difference between apple spawns (min 300px difference between the last spawn)
            while self.apple_collider_last + diff >= self.apple_collider.x and self.apple_collider_last - diff <= self.apple_collider.x :
                self.apple_collider.x = random.randrange(0, width)
                self.apple_collider.y = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_img = pygame.image.load("Goblin_idle.gif").convert_alpha()
        self.player_img = pygame.transform.scale(self.player_img, (100,100))
        self.player_rect = self.player_img.get_rect(topleft =  (player_x,player_y))
        self.player_vel = 7

    def player_movement(self):
        if self.keys[pygame.K_LEFT]:
            self.player_img = pygame.image.load("Goblin_run_left.gif").convert_alpha()
            self.player_img = pygame.transform.scale(self.player_img, (100,100))
            self.player_rect.right -= vel
        if self.keys[pygame.K_RIGHT]:
            self.player_img = pygame.image.load("Goblin_run_right.gif").convert_alpha()
            self.player_img = pygame.transform.scale(self.player_img, (100,100))
            self.player_rect.left += vel
        self.player_img = pygame.image.load("Goblin_idle.gif").convert_alpha()
        self.player_img = pygame.transform.scale(self.player_img, (100,100))

    def edge_colisions(self):
        if self.player_rect.x > width:
            self.player_rect.x = width
        if self.player_rect.x < 0:
            self.player_rect.x = 0

""""
def animation_left(player_rect):
    delay = 0.2
    current_index = 0
    list = []
    list.append(pygame.image.load(r"Left\left_0.jpg"))
    list.append(pygame.image.load(r"Left\left_1.jpg"))
    list.append(pygame.image.load(r"Left\left_2.jpg"))
    list.append(pygame.image.load(r"Left\left_3.jpg"))
    list.append(pygame.image.load(r"Left\left_4.jpg"))
    list.append(pygame.image.load(r"Left\left_5.jpg"))
    list.append(pygame.image.load(r"Left\left_6.jpg"))
    list.append(pygame.image.load(r"Left\left_7.jpg"))
    for current_index in list:
        current_index = current_index + 0.2
        player_rect = list[current_index]
        if int(current_index) >= len(list):
            current_index = 0
        player_rect = list[current_index]
        return player_rect
"""
pygame.init()
screen = pygame.display.set_mode((1196,596))
pygame.display.set_caption("Apple Rush")
clock = pygame.time.Clock()
font = pygame.font.Font("Pixeltype.ttf",50)
game_active = False

background_image = pygame.image.load("bg.jpg")
score = 0
player_x = 550
player_y = 410
vel = 7
width = 1100
height = 500

#groups
player = pygame.sprite.GroupSingle()
player.add(Player())

apples_group = pygame.sprite.Group()
apples_group.add(apple())
apples_group.add(apple())

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.fill("Black")

        if(score<=10):
            player.player_movement()

        
        scoreboard = font.render("Score: " + str(score), False, "Green")
        screen.blit(background_image, (0, 0))
        #screen.blit(player_img, player_rect)
        #screen.blit(scoreboard, (20, 20))
        #screen.blit(apples, (apple_collider.x,apple_collider.y))
        player_img = pygame.image.load("Goblin_idle.gif").convert_alpha()
        player_img = pygame.transform.scale(player_img, (100,100))

    pygame.display.update()
    clock.tick(60)
    