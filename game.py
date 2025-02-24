import pygame
from random import randrange
import os
import sys

pygame.init()
all_sprites = pygame.sprite.Group()
pygame.display.set_caption("Игра")
size = width, height = 800, 400
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Player(pygame.sprite.Sprite):
    image = load_image("test.png")

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.rect = self.rect.move(0, 1)


player = Player((10, 10))
background = load_image("background.png")

if __name__ == '__main__':

    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            all_sprites.draw(screen)
            all_sprites.update()
    pygame.quit()
