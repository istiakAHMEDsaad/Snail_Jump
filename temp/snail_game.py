import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(
            self,
    ):
        super().__init__()
        self.player_walk_1 = pygame.image.load(
            "./graphics/snail/stand.png"
        ).convert_alpha()
        self.player_walk_2 = pygame.image.load(
            "./graphics/snail/walk1.png"
        ).convert_alpha()
        self.player_walk_3 = pygame.image.load(
            "./graphics/snail/walk2.png"
        ).convert_alpha()
        self.player_walk_4 = pygame.image.load(
            "./graphics/snail/walk3.png"
        ).convert_alpha()
        self.player_index = 0
        self.walk = [self.player_walk_1, self.player_walk_2, self.player_walk_3, self.player_walk_4]
        self.player_jump = pygame.image.load("./graphics/snail/jump.png").convert_alpha()
        self.image = self.walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 260))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 250 and game_active:
            jump_sound.play()
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 250:
            self.rect.bottom = 250

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_animation()

    def player_animation(self):
        if self.rect.bottom < 250:
            self.image = self.player_jump

        else:
            self.player_index += 0.1
            if self.player_index >= len(self.walk):
                self.player_index = 0
            self.image = self.walk[int(self.player_index)]


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "fly":
            fly_frame_1 = pygame.image.load("./graphics/fly/fly1.png").convert_alpha()
            fly_frame_2 = pygame.image.load("./graphics/fly/fly2.png").convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 150

        else:
            enemy_frame_1 = pygame.image.load(
                "./graphics/bird/bird1.png"
            ).convert_alpha()
            enemy_frame_2 = pygame.image.load(
                "./graphics/bird/bird2.png"
            ).convert_alpha()
            self.frames = [enemy_frame_1, enemy_frame_2]
            y_pos = 250

        self.animation_index = 0

        self.image = self.frames[self.animation_index]

        self.rect = self.image.get_rect(midbottom=(randint(900, 1400), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0

        self.image = self.frames[int(self.animation_index)]

    def update(
            self,
    ):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


def display_score():
    current_time = pygame.time.get_ticks() // 1000 - starting_time
    score_surface = text_font.render(
        "score: " + str(current_time), False, (66, 32, 6)
    )
    score_rect = score_surface.get_rect(center=(400, 100))
    screen.blit(score_surface, score_rect)
    return current_time


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False

    return True


pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Snail Game")
clock = pygame.time.Clock()
game_active = False
starting_time = 0
score = 0

jump_sound = pygame.mixer.Sound("./audio/jump.mp3")
jump_sound.set_volume(0.2)

bg_music = pygame.mixer.Sound("./audio/background_music.mp3")
bg_music.set_volume(0.1)
bg_music.play(loops=-1)

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

text_font = pygame.font.Font("./fonts/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("./graphics/environment/sky.png").convert()
ground_surface = pygame.image.load("./graphics/environment/ground.png").convert()

player_stand_surface = pygame.image.load(
    "./graphics/snail/stand.png"
).convert_alpha()

player_stand_surface = pygame.transform.rotozoom(player_stand_surface, 0, 2)
player_stand_rect = player_stand_surface.get_rect(center=(400, 200))

text_surface = text_font.render("Snail Jump", False, (24, 24, 27))
text_rect = text_surface.get_rect(center=(400, 80))

massage_text = text_font.render("PRESS SPACE TO PLAY", False, (66, 32, 6))
massege_rect = massage_text.get_rect(center=(400, 350))

obstacle_timer = pygame.USEREVENT + 1

pygame.time.set_timer(obstacle_timer, 1500)

enemy_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(enemy_animation_timer, 300)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(["fly", "snail", "snail", "snail"])))

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    starting_time = pygame.time.get_ticks() // 1000

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 250))

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()
        score = display_score()

        game_active = collision_sprite()

    else:
        screen.fill((21, 128, 61))
        screen.blit(player_stand_surface, player_stand_rect)
        screen.blit(text_surface, text_rect)

        score_msg_surface = text_font.render(
            f"your score: {score}", False, (66, 32, 6)
        )
        score_msg_rect = score_msg_surface.get_rect(center=(400, 350))

        if score:
            screen.blit(score_msg_surface, score_msg_rect)

        else:
            screen.blit(massage_text, massege_rect)

    pygame.display.update()
    clock.tick(60)