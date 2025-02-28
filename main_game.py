import pygame
from sys import exit


pygame.init()

# initial display size
screen = pygame.display.set_mode((800, 400))
# set game title
pygame.display.set_caption('Jumpy Jumpy')
# set game frame rate
clock = pygame.time.Clock()

# sky surface
sky_surface = pygame.image.load('./graphics/environment/sky.png')
# ground surface
ground_surface = pygame.image.load('./graphics/environment/ground.png')
player_surface = pygame.image.load('./graphics/snail/stand.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # surface position (x, y)
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,250))
    screen.blit(player_surface,(0,200))
    pygame.display.update()
    clock.tick(60)