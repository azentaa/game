import pygame
import os
import sys
from random import randrange

pygame.init()
# создаем экран
pygame.display.set_caption("Игра в рыбку")
size = width, height = 900, 800
screen = pygame.display.set_mode(size)
# создаем группы спрайтов
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


# функции
def terminate():
    pygame.quit()
    sys.exit()

def text_set():
    font = pygame.font.Font(None, 50)
    text = font.render(str(round(timer / fps, 1)), 1, (100, 255, 100))
    text_x = width - 50
    text_y = 50
    screen.blit(text, (text_x, text_y))
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# классы
class Enemy(pygame.sprite.Sprite):
    image1 = load_image("enemy_sprite.png")
    image = pygame.transform.scale(image1, (50, 50))
    image.convert_alpha()
    # image_boom = load_image("boom.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Enemy.image
        self.rect = self.image.get_rect()
        self.rect.x = width - 200
        self.rect.y = randrange(height)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args):
        self.rect = self.rect.move(-10, 0)


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
    image1 = load_image("player_sprite.png")
    image = pygame.transform.scale(image1, (100, 50))
    image.convert_alpha()
    def __init__(self, pos, *group):
        super().__init__(*group)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEMOTION:
            self.rect.y = args[0].pos[1]
        if self.rect.y > width - 200:
            self.rect.y = width - 210
        if self.rect.y < 10:
            self.rect.y = 10
        if pygame.sprite.spritecollideany(self, enemy_sprites):
            terminate()


background = load_image("background.png")
Border(10, 10, width - 10, 10)
Border(10, height - 10, width - 10, height - 10)
Border(10, 10, 10, height - 10)
Player((150, 100), all_sprites, player_sprite)

SPAWNENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNENEMY, 1000)


text_x = width - 50
text_y = 50
font = pygame.font.Font(None, 50)
fps = 30
timer = 0
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWNENEMY:
            Enemy(all_sprites, enemy_sprites)
        if event.type == pygame.MOUSEMOTION:
            player_sprite.update(event)
    timer += 1
    a = str(round(timer / fps, 1))
    text = font.render(a, 1, (0, 0, 0))

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(fps)
    screen.blit(text, (text_x, text_y))
    pygame.display.flip()
pygame.quit()
