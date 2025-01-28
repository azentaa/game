import pygame

n = tuple(int(i) for i in input().split())

if __name__ == '__main__':
    pygame.init()
    size = width, height = n
    screen = pygame.display.set_mode(size)
    pygame.draw.line(screen, (255, 255, 255), (0, 0), n, width=5)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
