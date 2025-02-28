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
snail_rectangle = snailStand_surface.get_rect(midbottom=(80, 260))

# all bird surface
birdOne_surface = pygame.image.load('./graphics/bird/bird1.png').convert_alpha()
bird_rectangle = birdOne_surface.get_rect(midbottom=(700, 252))

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

        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print("press down")
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print("up")
        # if event.type == pygame.MOUSEMOTION:
        #     if snail_rectangle.collidepoint(event.pos):
        #         print('collision')
    # surface position (x, y)
    # ----------> environment <----------
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 250))

    # ----------> all about snail <----------
    screen.blit(snailStand_surface, snail_rectangle)
    if snail_rectangle.colliderect(bird_rectangle):
        print('snail have been eaten by a bird')

    # mouse_position = pygame.mouse.get_pos()
    # print(snail_rectangle.collidepoint(mouse_position))
    # print(pygame.mouse.get_pressed())

    # ----------> all about bird <----------
    screen.blit(birdOne_surface, bird_rectangle)
    bird_rectangle.x -= 4
    if bird_rectangle.right <= 0:
        bird_rectangle.left = 800

    # ----------> all fonts <----------
    screen.blit(text_surface, (320, 100))

    pygame.display.update()
    clock.tick(60)
