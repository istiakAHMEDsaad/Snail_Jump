import pygame
from sys import exit


pygame.init()

# initial display size
screen = pygame.display.set_mode((800, 400))
# set game title
pygame.display.set_caption('Jumpy Jumpy')
# set game frame rate
clock = pygame.time.Clock()

# surface size (H, W)
test_surface = pygame.Surface((100, 80))
# surface color
test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # surface position (x, y)
    screen.blit(test_surface,(0,0))
    pygame.display.update()
    clock.tick(60)