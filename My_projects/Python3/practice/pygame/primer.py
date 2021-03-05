#!/usr/bin/python3
import pygame
from pygame.locals import(
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
import random

pygame.init();

width, height = 800, 600;
screen = pygame.display.set_mode((width, height));
pygame.display.set_caption("Primer");

clock = pygame.time.Clock();

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__();
        self.surf = pygame.Surface((50, 50));
        self.surf.fill(pygame.Color("black"));
        self.rect = self.surf.get_rect();

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5);
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5);
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0);
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0);

        if self.rect.left < 0:
            self.rect.left = 0;
        if self.rect.right > width:
            self.rect.right = width;
        if self.rect.top <= 0:
            self.rect.top = 0;
        if self.rect.bottom >= height:
            self.rect.bottom = height;

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemy, self).__init__();
        self.surf = pygame.Surface((25, 25));
        self.surf.fill(pygame.Color("blue"));
        self.rect = self.surf.get_rect(
            center = (
                random.randint(width + 20, width + 100),
                random.randint(0, height)
            )
        );
        self.speed = random.randint(5, 20);

    def update(self):
        self.rect.move_ip(-self.speed, 0);
        if self.rect.right < 0:
            self.kill();

add_enemy = pygame.USEREVENT + 1;
pygame.time.set_timer(add_enemy, 250);

player = Player();
enemies = pygame.sprite.Group();
all_sprites = pygame.sprite.Group();
all_sprites.add(player);

def game_loop():
    running = True;
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False;

            # Add a new enemy
            elif event.type == add_enemy:
                # Create a new enemy and sprite groups
                new_enemy = Enemy();
                enemies.add(new_enemy);
                all_sprites.add(new_enemy);

        screen.fill(pygame.Color("white"));

        # Billentyű konfigurálása
        pressed_keys = pygame.key.get_pressed();
        player.update(pressed_keys);

        # Ellenség poziciójának feltöltése
        enemies.update();

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect);

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(player, enemies):
            # Game over and stop the loop
            player.kill();
            running = False;

        screen.blit(player.surf, player.rect);

        pygame.display.update();
        clock.tick(60);

    pygame.quit();

game_loop();

quit();