import os
import sys

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)



image = pygame.image.load(fullname)

while True:
    sprite = pygame.sprite.Sprite()
    # определим его вид
    sprite.image = load_image("test.png")

    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 5
    sprite.rect.y = 20
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break