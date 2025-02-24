import pygame
import os
import sys
import random

if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)


    def load_image(name, colorkey=None):
        fullname = os.path.join('..\data', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image


    class Bomb(pygame.sprite.Sprite):
        image = load_image("test.png")
        image_boom = load_image("test.png")

        def __init__(self, group):
            super().__init__(group)
            self.image = Bomb.image
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(width)
            self.rect.y = random.randrange(height)

        def update(self, *args):
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                    self.rect.collidepoint(args[0].pos):
                self.image = self.image_boom


    running = True
    all_sprites = pygame.sprite.Group()
    for i in range(20):
        Bomb(all_sprites)
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in all_sprites:
                    all_sprites.update(event)
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
    pygame.quit()