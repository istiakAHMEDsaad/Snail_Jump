import pygame
from sys import exit


pygame.init()

# ----------> initial display size <----------
screen = pygame.display.set_mode((800, 400))

# ----------> set game title <----------
pygame.display.set_caption('Snail Jump')

# ----------> set game frame rate <----------
clock = pygame.time.Clock()

# ----------> fonts <----------
text_font = pygame.font.Font('./fonts/Pixeltype.ttf', 50)



# ----------> All surface <----------
# sky surface
sky_surface = pygame.image.load('./graphics/environment/sky.png').convert()
# ground surface
ground_surface = pygame.image.load('./graphics/environment/ground.png').convert()
# all snail surface
snailStand_surface = pygame.image.load('./graphics/snail/stand.png').convert_alpha()
# all bird surface
birdOne_surface = pygame.image.load('./graphics/bird/bird1.png').convert_alpha()
# text surface
text_surface = text_font.render('Snail Jump', False, '#27272A')

# ----------> Position <----------
bird_x_position = 700

# ----------> MAIN <----------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # surface position (x, y)
    # ----------> environment <----------
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,250))

    # ----------> all about snail <----------
    screen.blit(snailStand_surface,(20,178))
    screen.blit(birdOne_surface,(bird_x_position,212))
    bird_x_position -= 4
    if bird_x_position < -50:
        bird_x_position = 900

    # ----------> all about bird <----------
    screen.blit(text_surface,(320, 100))
    pygame.display.update()
    clock.tick(60)