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


# ===================================> collision function
def collision(player, obstacle):
    if obstacle:
        for obstacle_rectangle in obstacle:
            if player.colliderect(obstacle_rectangle):
                return False

    return True


def player_animation():
    global player_surface, player_index
    if player_rectangle.bottom < 252:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]


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

player_walk_1 = pygame.image.load('./graphics/snail/walk1.png').convert_alpha()
player_walk_2 = pygame.image.load('./graphics/snail/stand.png').convert_alpha()
player_walk_3 = pygame.image.load('./graphics/snail/walk2.png').convert_alpha()
player_walk_4 = pygame.image.load('./graphics/snail/walk3.png').convert_alpha()
player_jump = pygame.image.load('./graphics/snail/jump.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4]
player_index = 0
player_surface = player_walk[player_index]
player_stand_surface = pygame.image.load('./graphics/snail/stand.png').convert_alpha()

birdOne_surface = pygame.image.load('./graphics/bird/bird1.png').convert_alpha()
menu_player_surface = pygame.image.load('./graphics/snail/stand.png').convert_alpha()
fly_surface = pygame.image.load('./graphics/fly/fly1.png').convert_alpha()

# ===================================> rectangle position (enemy & player)
player_rectangle = player_surface.get_rect(midbottom=(80, 260))

# ===================================> image transformation
menu_player_scaled = pygame.transform.rotozoom(menu_player_surface, 0, 2)

# ===================================> rectangle position
text_surface = text_font.render('Snail Jump', False, (24, 24, 27))
menu_text = text_surface.get_rect(center=(400, 110))
message_text = text_font.render("PRESS SPACE TO PLAY", False, (66, 32, 6))
message_rectangle = message_text.get_rect(center=(400, 350))
menu_player_rectangle = menu_player_scaled.get_rect(center=(400, 200))
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
                if event.key == pygame.K_SPACE and player_rectangle.bottom == 260:
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

        # ----------> all about player <----------
        score = display_score()
        gravity += 1
        player_rectangle.y += gravity
        if player_rectangle.bottom >= 260:
            player_rectangle.bottom = 260

        player_animation()
        screen.blit(player_surface, player_rectangle)

        # ----------> all about enemy <----------
        obstacle_rectangle_list = obstacle_movement(obstacle_rectangle_list)
        game_active = collision(player_rectangle, obstacle_rectangle_list)

    else:
        screen.fill((21, 128, 61))
        screen.blit(menu_player_scaled, menu_player_rectangle)
        screen.blit(text_surface, menu_text)

        score_message_surface = text_font.render(f"Highest Score: {score}", False, (24, 24, 27))
        score_message_rectangle = score_message_surface.get_rect(center=(400, 350))

        if not score:
            screen.blit(message_text, message_rectangle)
        else:
            screen.blit(score_message_surface, score_message_rectangle)

        obstacle_rectangle_list.clear()
        player_rectangle.midbottom = (80, 260)
        gravity = 0

    pygame.display.update()
    clock.tick(60)
