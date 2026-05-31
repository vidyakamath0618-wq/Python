import math
import random
import pygame
#constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
#Initialise pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Background
background = pygame.image.load('background.png')
#caption and icon
pygame.display.set_caption("space invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
#player
playerImg = pygame.image.load('player.png')
playerx = PLAYER_START_X
playery = PLAYER_START_Y
playerx_change = 0
#enemy
enemyImg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6
for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, SCREEN_WIDTH - 64))#64 is the size of the enemy
    enemyy.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyx_change.append