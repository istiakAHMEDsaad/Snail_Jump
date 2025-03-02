# ===================================> import
import pygame
from sys import exit
from random import randint


# ===================================> display score
def display_score():
    current_time = pygame.time.get_ticks() // 1000 - starting_time
    score_surface = text_font.render("Score: " + str(current_time), False, (39, 39, 42))
    score_rectangle = score_surface.get_rect(center=(400, 100))
    screen.blit(score_surface, score_rectangle)
    return current_time


# ===================================> movement function
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rectangle in obstacle_list:
            obstacle_rectangle.x -= 6

            if obstacle_rectangle.bottom == 252:
                screen.blit(birdOne_surface, obstacle_rectangle)

            else:
                screen.blit(fly_surface, obstacle_rectangle)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []


# collision function
def collision(player, obstacle):
    if obstacle:
        for obstacle_rectangle in obstacle:
            if player.colliderect(obstacle_rectangle):
                return False

    return True


pygame.init()

# ===================================> display size
screen = pygame.display.set_mode((800, 400))

# ===================================> game title
pygame.display.set_caption('Snail Jump')

# ===================================> game frame time & others
clock = pygame.time.Clock()
gravity = 0
game_active = False
starting_time = 0
score = 0

# ===================================> import assets
text_font = pygame.font.Font('./fonts/Pixeltype.ttf', 50)
sky_surface = pygame.image.load('./graphics/environment/sky.png').convert()
ground_surface = pygame.image.load('./graphics/environment/ground.png').convert()
snailStand_surface = pygame.image.load('./graphics/snail/walk1.png').convert_alpha()
birdOne_surface = pygame.image.load('./graphics/bird/bird1.png').convert_alpha()
menu_snail_surface = pygame.image.load('./graphics/snail/stand.png').convert_alpha()
fly_surface = pygame.image.load('./graphics/fly/fly1.png').convert_alpha()

# ===================================> rectangle position (bird & snail)
snail_rectangle = snailStand_surface.get_rect(midbottom=(80, 260))

# ===================================> image transformation
menu_snail_scaled = pygame.transform.rotozoom(menu_snail_surface, 0, 2)

# ===================================> rectangle position
text_surface = text_font.render('Snail Jump', False, (24, 24, 27))
menu_text = text_surface.get_rect(center=(400, 110))
message_text = text_font.render("PRESS SPACE TO PLAY", False, (66, 32, 6))
message_rectangle = message_text.get_rect(center=(400, 350))
menu_snail_rectangle = menu_snail_scaled.get_rect(center=(400, 200))
obstacle_rectangle_list = []

# ===================================> user event
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# ===================================> main part
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
                    starting_time = pygame.time.get_ticks() // 1000

        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                obstacle_rectangle_list.append(birdOne_surface.get_rect(midbottom=(randint(900, 1400), 252)))
            else:
                obstacle_rectangle_list.append(fly_surface.get_rect(midbottom=(randint(900, 1400), 152)))

    # ===================================> object blit
    if game_active:
        # surface position (x, y)
        # ----------> environment <----------
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 250))

        # ----------> all about snail <----------
        screen.blit(snailStand_surface, snail_rectangle)
        score = display_score()
        gravity += 1
        snail_rectangle.y += gravity
        if snail_rectangle.bottom >= 260:
            snail_rectangle.bottom = 260

        # ----------> all about bird <----------
        obstacle_rectangle_list = obstacle_movement(obstacle_rectangle_list)
        game_active = collision(snail_rectangle, obstacle_rectangle_list)

    else:
        screen.fill((21, 128, 61))
        screen.blit(menu_snail_scaled, menu_snail_rectangle)
        screen.blit(text_surface, menu_text)

        score_message_surface = text_font.render(f"Highest Score: {score}", False, (24, 24, 27))
        score_message_rectangle = score_message_surface.get_rect(center = (400, 350))

        if not score:
            screen.blit(message_text, message_rectangle)
        else:
            screen.blit(score_message_surface, score_message_rectangle)

        obstacle_rectangle_list.clear()
        snail_rectangle.midbottom = (80, 260)
        gravity = 0

    pygame.display.update()
    clock.tick(60)
