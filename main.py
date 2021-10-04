import sys
import pygame
from snake import Snake
from food import Food

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = (45, 45, 45)

clock = pygame.time.Clock()
FPS = 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("The Snake Game")

snake_parts = pygame.sprite.Group()
snake = Snake("head")
snake.set_rounded(8)
snake.rect.center = (285, 285)
snake_parts.add(snake)

food_list = pygame.sprite.Group()


def main():

    food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
    food_list.add(food)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if snake.moving_down:
                        continue
                    snake.reset_moving_flags()
                    snake.moving_up = True
                elif event.key == pygame.K_DOWN:
                    if snake.moving_up:
                        continue
                    snake.reset_moving_flags()
                    snake.moving_down = True
                elif event.key == pygame.K_LEFT:
                    if snake.moving_right:
                        continue
                    snake.reset_moving_flags()
                    snake.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    if snake.moving_left:
                        continue
                    snake.reset_moving_flags()
                    snake.moving_right = True

        screen.fill(SCREEN_BG_COLOR)

        food_list.draw(screen)
        snake_parts.draw(screen)

        if len(food_list) < 1:
            food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
            food_list.add(food)

        if food.collision_check(snake):
            food.kill()
            food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
            food_list.add(food)

        snake.update()

        pygame.display.update()
        clock.tick(FPS)


main()
pygame.quit()
