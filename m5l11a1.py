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
    enemyx_change.append(ENEMY_SPEED_X)
    enemyy_change.append(ENEMY_SPEED_X)
#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
buuletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"
#score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10
#game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)
def show_score(x, y):
    #display the current score on the screen
    score = font.render("Score :" + str(score_value),True,(255, 255, 255))
    screen.blit(score,(x, y))
def game_over_text():
    #display the game over text
    over_text = over_font.render("GAME OVER", True,(255, 255, 255))
    screen.blit(over_text, (200, 250))
def player(x, y):
    #draw the player on the screen
    screen.blit(playerImg, (x, y))
def enemy(x, y, i):
    #draw an enemy on the screen
    screen.blit(enemyImg[i], (x, y))
def fire_bullet(x, y):
    #fire a bullet from the player's position
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    #check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    return distance < COLLISION_DISTANCE
#game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_left:
               playerx_change = -5
           if event.key == pygame.K_right:
               playerx_change = 5