import pygame
import os
import sys
from random import randrange

pygame.init()
all_sprites = pygame.sprite.Group()
pygame.display.set_caption("Игра")
size = width, height = 800, 400
screen = pygame.display.set_mode(size)


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
        self.rect.x = width
        self.rect.y = randrange(height)

    def update(self, *args):
        self.rect = self.rect.move(1, 0)


class Player(pygame.sprite.Sprite):
    image = load_image("test.png")

    def __init__(self, pos, *group):
        super().__init__(*group)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.rect = self.rect.move(0, 1)

SPAWNENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNENEMY, 1)
background = load_image("background.png")
Player((10, 10), all_sprites)
running = True
while running:
    # внутри игрового цикла ещё один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWNENEMY:
            Enemy(all_sprites)

        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
pygame.quit()
