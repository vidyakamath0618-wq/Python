import pygame
#initialising pygame and screen dimensions
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
#initialize display surface and set title
display_surface = pygame.display.set_model((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('adding image and background image')
#loadand scale images directly
background_image = pygame.transform.scale(pygame.image.load('background.png').convert(),(SCREEN_WIDTH, SCREEN_HEIGHT))
penguin_image = pygame.transform.scale(pygame.image.load('penguin.png').convert_alpha(), (200, 200))
penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
#Initialize font, render text, and set text position
text = pygame.font.Font(None, 36).render('hello World', True,pygame.colour('black'))
text_rect = text
