# библиотеки
import pygame
import os
import sys
from random import randrange, randint

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

# выход из программы
def terminate():
    pygame.quit()
    sys.exit()


# функция для удобства
def one_frame(a):
    text = font.render(a, 1, (0, 0, 0))
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(fps)
    screen.blit(text, (text_x, text_y))
    pygame.display.flip()


# установка параметров текста таймера
def text_set():
    font = pygame.font.Font(None, 50)
    text = font.render(str(round(timer / fps, 1)), 1, (100, 255, 100))
    text_x = width - 50
    text_y = 50
    screen.blit(text, (text_x, text_y))


# обработка изображений
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# начальный экран
def start_screen():
    intro_text = ["Игра в рыбку", "",
                  "Правила игры",
                  "Для перемещения двигайте мышью",
                  "вверх и вниз. Обходите медуз."]

    fon = pygame.transform.scale(load_image('background.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(fps)


# конечный экран
def end_screen(score):
    intro_text = ["Вы столкнулись с медузой!", "",
                  "Ваш счет:",
                  f"{score} секунд! Вы молодец!"]

    fon = pygame.transform.scale(load_image('background.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(fps)


# классы

# класс врага
class Enemy(pygame.sprite.Sprite):
    image1 = load_image("enemy.png")
    image = pygame.transform.scale(image1, (350, 50))
    image.convert_alpha()

    def __init__(self, *group):
        super().__init__(*group)
        self.frames = []
        self.cut_sheet(self.image, 4, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(width, randrange(height - 100))

        # self.image = Enemy.image
        # self.rect = self.image.get_rect()
        # self.rect.x = width - 300
        # self.rect.y = randrange(height)
        # self.mask = pygame.mask.from_surface(self.image)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *args):
        #
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(-10, 0)


# класс границ
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


# класс игрока
class Player(pygame.sprite.Sprite):
    image1 = load_image("player.png")
    image = pygame.transform.scale(image1, (384, 46))
    image.convert_alpha()

    def __init__(self, columns, rows, x, y, *group):
        super().__init__(*group)
        self.frames = []
        self.cut_sheet(self.image, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        # self.image = Player.image
        # self.rect = self.image.get_rect()
        # self.rect.x = pos[0]
        # self.rect.y = pos[1]
        # self.mask = pygame.mask.from_surface(self.image)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *args):
        # смена кадров
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        # управление и ограничение
        if args and args[0].type == pygame.MOUSEMOTION:
            self.rect.y = args[0].pos[1]
        if self.rect.y > width - 200:
            self.rect.y = width - 210
        if self.rect.y < 10:
            self.rect.y = 10
        # обработка коллизии с врагом
        if pygame.sprite.spritecollideany(self, enemy_sprites):
            global game_end
            game_end = True


# переменные и константы
background = load_image("background.png")
spawn_timer = randrange(1000, 2001, 500)
text_x = width - 150
text_y = 50
font = pygame.font.Font(None, 50)
fps = 20
timer = 0
clock = pygame.time.Clock()
score = ""

# расставляем спрайты
Border(10, 10, width - 10, 10)
Border(10, height - 10, width - 10, height - 10)
Border(10, 10, 10, height - 10)
Player(4, 1, 150, 100, all_sprites, player_sprite)
# событие спавна медузы
SPAWNENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNENEMY, spawn_timer)

# триггеры
running = True
game_end = False

start_screen()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWNENEMY:
            for _ in range(randint(1, 3)):
                Enemy(all_sprites, enemy_sprites)
        if event.type == pygame.MOUSEMOTION:
            player_sprite.update(event)
    if not game_end:
        timer += 1
        score = str(round(timer / fps, 1))
        one_frame(score)
    else:
        end_screen(score)
pygame.quit()
