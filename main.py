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

# Groups that store objects
snake_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()

# Instantiate the snake object
snake = Snake()
snake.set_rounded(8)
snake.rect.center = (285, 285)
snake_group.add(snake)


def main():
    """Main game loop"""

    # Instantiate the first food object
    food = Food(SCREEN_WIDTH, snake.rect.width)
    food_group.add(food)

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

        if food.is_collided(snake):
            food.remove(food_group)
            food = food.create_food(food_group, SCREEN_WIDTH, snake.rect.width)

        # Run snake class update method
        snake.update()

        # Refresh display on each frame
        pygame.display.update()
        # Set FPS value
        clock.tick(FPS)


main()
pygame.quit()
