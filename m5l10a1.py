import pygame
import random
#constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72
#Initialize pygame
pygame.init()
#load and transform the background image
background_image = pygame.transform.scale(pygame.image.load("bg.jpg"),
                                          (SCREEN_WIDTH, SCREEN_HEIGHT))
#load font once at the beginning
font = pygame.font.SysFont("Times new roman", FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.surface([width, height])
        self.image.fill(
            pygame.color('dogerblue')) #background color of sprite
        pygame.draw.rect(self.image, color, pygame.rect(0,0, width, height))
        self.rect = self.image.get_rect()
        def move(self, x_change, y_change):
            self.rect.x = max(
                min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)