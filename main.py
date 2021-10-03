import pygame
from snake import Snake

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = (45, 45, 45)

clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("The Snake Game")

snake_parts = pygame.sprite.Group()
snake = Snake()
snake.set_rounded(8)
snake.rect.center = screen.get_rect().center
snake_parts.add(snake)


def main():

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass

        screen.fill(SCREEN_BG_COLOR)
        snake_parts.draw(screen)
        snake.move()

        pygame.display.update()
        clock.tick(FPS)


main()
pygame.quit()
