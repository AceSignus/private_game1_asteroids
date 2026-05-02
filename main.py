import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():
    print("Starting Asteroids...")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        if event.type == pygame.QUIT:
            return
        screen.fill((100, 10, 10))
        pygame.display.flip()
        millisecon_counter = clock.tick(60)
        dt = millisecon_counter / 1000.0
        #print(dt)




if __name__ == "__main__":
    main()



