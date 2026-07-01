import pygame
import sys
from bombs import Bomb
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCORE_NUMBER
from player import Player
from logger import log_state, log_event
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids...")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Bomb.containers = (bombs, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    score = 0
    font = pygame.font.Font(None, 36)
    
    
    while True:
        log_state()
        for event in pygame.event.get():
            log_event("event")
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        for item in asteroids:
            for shot in shots:
                if shot.collides_with(item):
                    log_event("asteroid_shot")
                    item.split()
                    shot.kill()
                    score += SCORE_NUMBER // item.radius
            for bomb in bombs:
                if bomb.collides_with(item):
                    log_event("asteroid_bombed")
                    item.kill()
                    bomb.kill()
                    score += item.radius // 10
        for item in asteroids:
            if player.collides_with(item):
                log_event("player_hit")
                print("Game over!")
                print(f"Final score: {score}")
                sys.exit()
        score_surface = font.render(f"Score: {score}", True, "white")
        screen.blit(score_surface, (10, 10))

        pygame.display.flip() # Happens after all the drawing is done
        
        millisecon_counter = clock.tick(60)
        dt = millisecon_counter / 1000.0



if __name__ == "__main__":
    main()






