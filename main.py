import sys
import pygame
from pygame.locals import *
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

# Groups that store objects
snake_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()

# Instantiate the snake head
snake = Snake()
snake.tag = "head"
snake.rect.center = (285, 285)
snake_group.add(snake)


def main():
    """Main game loop"""

    # Instantiate the first food object
    food = Food(SCREEN_WIDTH, snake.rect.width)
    food_group.add(food)

    # Set allowed input events
    pygame.event.set_allowed(QUIT)
    pygame.event.set_allowed(KEYDOWN)

    while True:
        # Check user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check for user keyboard presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.move_up()
                elif event.key == pygame.K_DOWN:
                    snake.move_down()
                elif event.key == pygame.K_LEFT:
                    snake.move_left()
                elif event.key == pygame.K_RIGHT:
                    snake.move_right()

        # Screen background color
        screen.fill(SCREEN_BG_COLOR)

        # Draw the objects from groups on screen
        food_group.draw(screen)
        snake_group.draw(screen)

        # Make body follow the head
        snake.follow_head(snake_group)
        # Move & control the snake head
        snake.update()

        # Check if snake has collided with food
        if food.is_collided(snake):
            # Remove food from ground
            food.remove(food_group)
            # Create new food on a random position
            food = food.create_food(food_group, SCREEN_WIDTH, snake.rect.width)
            # Prolong the snake body by 1
            snake.create_new_body(snake_group)

        # Refresh display on each frame
        pygame.display.update()
        # Set FPS value
        clock.tick(FPS)


main()
pygame.quit()
