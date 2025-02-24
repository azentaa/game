import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        color = pygame.Color(255, 255, 255)
        y = self.top
        for i in range(self.height):
            x = self.left
            for j in range(self.width):
                f, b = self.get_cell((x, y))
                fill_cell = self.board[b][f]
                pygame.draw.rect(screen, color,
                                 (x, y, self.cell_size, self.cell_size), abs(fill_cell -1))
                x += self.cell_size
            y += self.cell_size

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if x in range(self.left, self.left + (self.cell_size * self.width)) and y in range(
                self.top, self.top + (self.cell_size * self.height)):
            x //= self.cell_size
            y //= self.cell_size
            return x, y
        return None

    def on_click(self, cell_coords):
        if cell_coords is not None:
            x, y = cell_coords
            if self.board[y][x] == 0:
                self.board[y][x] = 1
            else:
                self.board[y][x] = 0





pygame.init()
    # размеры окна:
size = width, height = 800, 600
    # screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
board = Board(5, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:

            a = board.get_cell(event.pos)
            board.on_click(a)
            print(board.board[a[1]])