import pygame


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = (30, 30, 30)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("The Snake Game")


def main():

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill(SCREEN_BG_COLOR)
        pygame.display.update()


main()
pygame.quit()
