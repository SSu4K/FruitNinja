import pygame
import random
from blade import Blade
from fruit import Fruit

BACKGROUND_COLOR = (25, 25, 25)
WHITE = (255, 255, 255)
RED = (200, 50, 100)
GREEN = (50, 200, 100)

FRAMERATE = 60
DT = 1/FRAMERATE
BLADE_LENGTH = 300
MAX_POINTS = BLADE_LENGTH // FRAMERATE

WINDOW_SIZE = (500, 500)

window = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
surface = pygame.display.get_surface()
fpsClock = pygame.time.Clock()

def draw_fruit(fruit: Fruit):
    pygame.draw.circle(surface, fruit.color, fruit.pos, fruit.size, fruit.size)

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
        if(random.randint(0, 1000)<30):
            size = random.randint(10, 20)
            pos = [random.randint(0, WINDOW_SIZE[0]), WINDOW_SIZE[1]]
            speed = [random.randint(-5, 5), random.randint(-18, -5)]
            fruits.append(Fruit(size, GREEN, pos, speed))

        surface.fill(BACKGROUND_COLOR)
        for fruit in fruits:
            if not fruit.is_in_bound(WINDOW_SIZE):
                fruits.remove(fruit)
                continue
            fruit.move(DT)
            draw_fruit(fruit)
        pygame.draw.lines(surface, WHITE, False, blade.get_points())

        pygame.display.flip()
        print(len(fruits))
        fpsClock.tick(FRAMERATE)

def main():

    pygame.init()
    loop()

if __name__ == "__main__":
    main()
