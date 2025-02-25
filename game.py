import pygame
import os
import sys
from random import randrange

pygame.init()
all_sprites = pygame.sprite.Group()
pygame.display.set_caption("Игра")
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Enemy(pygame.sprite.Sprite):
    image = load_image("test.png")

    # image_boom = load_image("boom.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Enemy.image
        self.rect = self.image.get_rect()
        self.rect.x = width - 200
        self.rect.y = randrange(height)
        self.group = group



    def update(self, *args):
        self.rect = self.rect.move(-1, 0)


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Player(pygame.sprite.Sprite):
    image = load_image("test.png")

    def __init__(self, pos, *group):
        super().__init__(*group)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, *args):
        if not pygame.sprite.spritecollideany(self, horizontal_borders):
            if args and args[0].type == pygame.MOUSEBUTTONDOWN:
                self.rect = self.rect.move(0, 1)
            else:
                self.rect = self.rect.move(0, -1)


Border(3, 3, width - 3, 3)
Border(3, height - 3, width - 3, height - 3)
Border(3, 3, 3, height - 3)
SPAWNENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNENEMY, 3000)
background = load_image("background.png")
player_sprite = pygame.sprite.Sprite()
Player((10, 10), all_sprites)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWNENEMY:
            Enemy(all_sprites)

        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
    pygame.display.flip()
pygame.quit()
