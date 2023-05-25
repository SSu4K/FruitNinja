import pygame
import random
from blade import Blade
from fruit import Fruit

BACKGROUND_COLOR = (25, 25, 25)
WHITE = (255, 255, 255)
RED = (200, 50, 100)
FRAMERATE = 60
DT = 1/FRAMERATE
BLADE_LENGTH = 500
MAX_POINTS = BLADE_LENGTH // FRAMERATE

WINDOW_SIZE = (500, 500)

window = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
surface = pygame.display.get_surface()
fpsClock = pygame.time.Clock()

def draw_fruit(fruit: Fruit):
    pygame.draw.circle(surface, fruit.color, fruit.pos, fruit.size, 1)

def loop():
    run = True
    blade = Blade(MAX_POINTS)
    fruits = []
    while(run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        mouse_pos = pygame.mouse.get_pos()
        blade.add_point(mouse_pos)
        if(random.randint(0, 1000)<100):
            fruits.append(Fruit(random.randint(10, 20), RED, [random.randint(0, WINDOW_SIZE[0]), WINDOW_SIZE[1]], [random.randint(-10, 10), random.randint(-15, -5)]))

        surface.fill(BACKGROUND_COLOR)
        for fruit in fruits:
            fruit.move(DT)
            draw_fruit(fruit)
        pygame.draw.lines(surface, WHITE, False, blade.get_points())

        pygame.display.flip()
        fpsClock.tick(FRAMERATE)

def main():
    '''
    Contains main game loop
    '''
    pygame.init()
    loop()

if __name__ == "__main__":
    main()
