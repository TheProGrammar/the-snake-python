import sys
import pygame
from snake import Snake
from food import Food

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = (45, 45, 45)

# Instantiate screen settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("The Snake Game")

# Set a clock for game speed settings
clock = pygame.time.Clock()
FPS = 5

snake_list = pygame.sprite.Group()
food_list = pygame.sprite.Group()

snake = Snake()
snake.set_rounded(8)
snake.rect.center = (285, 285)
snake_list.add(snake)


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
                    snake.move_up()
                elif event.key == pygame.K_DOWN:
                    snake.move_down()
                elif event.key == pygame.K_LEFT:
                    snake.move_left()
                elif event.key == pygame.K_RIGHT:
                    snake.move_right()

        screen.fill(SCREEN_BG_COLOR)

        food_list.draw(screen)
        snake_list.draw(screen)

        if food.is_collided(snake):
            food.remove(food_list)
            food = food.create_food(food_list, SCREEN_WIDTH, SCREEN_HEIGHT)

        snake.update()

        pygame.display.update()
        clock.tick(FPS)


main()
pygame.quit()
