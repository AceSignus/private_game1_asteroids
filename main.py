import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH
from player import Player
from logger import log_state


def main():
    print("Starting Asteroids...")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        if event.type == pygame.QUIT:
            return
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        for item in updatable:
            item.update(dt)

        pygame.display.flip() # Happens after all the drawing is done
        
        millisecon_counter = clock.tick(60)
        dt = millisecon_counter / 1000.0



if __name__ == "__main__":
    main()






