import pygame
import sys



def main_menu(screen):
    font_title = pygame.font.SysFont("Arial", 64)
    font_controls = pygame.font.SysFont("Arial", 28)

    title_text = font_title.render("ASTEROIDS", True, (255, 255, 255))

    controls = [
        "WASD - Rotate & Thrust",
        "Spacebar          - Shoot",
        "B - Drop Bomb",
        "Press ENTER to Play",
    ]

    while True:
        screen.fill((0, 0, 0))

        # Draw title
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))

        # Draw controls
        for i, line in enumerate(controls):
            rendered = font_controls.render(line, True, (200, 200, 200))
            screen.blit(rendered, (screen.get_width() // 2 - rendered.get_width() // 2, 250 + i * 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Exit menu, start game