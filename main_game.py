import pygame
from sys import exit
from pygame import K_SPACE


def display_score():
    current_time = pygame.time.get_ticks() // 1000 - starting_time
    score_surface = text_font.render("Score: " + str(current_time), False, (39, 39, 42))
    score_rectangle = score_surface.get_rect(center=(400, 100))
    screen.blit(score_surface, score_rectangle)


pygame.init()

# ----------> initial display size <----------
screen = pygame.display.set_mode((800, 400))

# ----------> set game title <----------
pygame.display.set_caption('Snail Jump')

# ----------> set game frame rate <----------
clock = pygame.time.Clock()
gravity = 0
game_active = False
starting_time = 0

# ----------> fonts <----------
text_font = pygame.font.Font('./fonts/Pixeltype.ttf', 50)

# ----------> All surface <----------
# sky surface
sky_surface = pygame.image.load('./graphics/environment/sky.png').convert()

# ground surface
ground_surface = pygame.image.load('./graphics/environment/ground.png').convert()

# all snail surface
snailStand_surface = pygame.image.load('./graphics/snail/walk1.png').convert_alpha()
snail_rectangle = snailStand_surface.get_rect(midbottom=(80, 260))

# all bird surface
birdOne_surface = pygame.image.load('./graphics/bird/bird1.png').convert_alpha()
bird_rectangle = birdOne_surface.get_rect(midbottom=(700, 252))

# text surface
text_surface = text_font.render('Snail Jump', False, (24,24,27))
menu_text = text_surface.get_rect(center = (400, 110))
message_text =  text_font.render("PRESS SPACE TO PLAY", False, (66,32,6))
message_rectangle = message_text.get_rect(center=(400, 350))

# menu
menu_snail_surface = pygame.image.load('./graphics/snail/stand.png').convert_alpha()
menu_snail_scaled = pygame.transform.rotozoom(menu_snail_surface, 0, 2)
menu_snail_rectangle = menu_snail_scaled.get_rect(center=(400, 200))

# ----------> Position <----------
bird_x_position = 700

# ----------> MAIN <----------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and snail_rectangle.bottom == 260:
                    gravity = -20

            if event.type == pygame.KEYUP:
                pass
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    bird_rectangle.left = 800
                    starting_time = pygame.time.get_ticks() // 1000

    if game_active:
        # surface position (x, y)
        # ----------> environment <----------
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 250))

        # ----------> all fonts <----------
        # screen.blit(text_surface, (320, 100))

        # ----------> all about snail <----------
        screen.blit(snailStand_surface, snail_rectangle)
        display_score()
        gravity += 1
        snail_rectangle.y += gravity
        if snail_rectangle.bottom >= 260:
            snail_rectangle.bottom = 260

        # ----------> all about bird <----------
        screen.blit(birdOne_surface, bird_rectangle)
        bird_rectangle.x -= 6
        if bird_rectangle.right <= 0:
            bird_rectangle.left = 800

        if bird_rectangle.colliderect(snail_rectangle):
            # pygame.quit()
            # exit()
            game_active = False
    else:
        screen.fill((21,128,61))
        screen.blit(menu_snail_scaled, menu_snail_rectangle)
        screen.blit(text_surface, menu_text)
        screen.blit(message_text, message_rectangle)

    pygame.display.update()
    clock.tick(60)

# --------------> Logic <--------------
# if event.type == pygame.MOUSEMOTION:
#     print(event.pos)
# if event.type == pygame.MOUSEBUTTONDOWN:
#     print("press down")
# if event.type == pygame.MOUSEBUTTONUP:
#     print("up")
# if event.type == pygame.MOUSEMOTION:
#     if snail_rectangle.collidepoint(event.pos):
#         print('collision')

# if snail_rectangle.colliderect(bird_rectangle):
#     print('collision')

# mouse_position = pygame.mouse.get_pos()
# print(snail_rectangle.collidepoint(mouse_position))
# print(pygame.mouse.get_pressed())

# keys = pygame.key.get_pressed()
#     if keys[pygame.K_SPACE]:
#         print("jump")
