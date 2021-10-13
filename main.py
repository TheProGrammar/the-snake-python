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
icon = pygame.image.load("assets/images/game_icon.png").convert_alpha()
pygame.display.set_icon(icon)
pygame.display.set_caption("The Snake Game")
pygame.mouse.set_visible(False)

# Load images
background = pygame.image.load("assets/images/grass_walls.png").convert()

# Load sounds
bg_music = pygame.mixer.Sound("assets/sounds/background_music.mp3")
move_fx = pygame.mixer.Sound("assets/sounds/move_sound.wav")
crunch_fx = pygame.mixer.Sound("assets/sounds/crunch_sound.wav")
game_over_fx = pygame.mixer.Sound("assets/sounds/game_over_fx.wav")

# Sound settings
pygame.mixer.Sound.set_volume(bg_music, 0.5)

# Set a clock for game speed settings
clock = pygame.time.Clock()
FPS = 5

# Groups that store objects
snake_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()

# Instantiate the snake head
snake = Snake(pygame.image.load("assets/images/head_brown.png"))
snake.rect.center = (285, 285)
snake_group.add(snake)

# Initialize the sound mixer
pygame.mixer.init()


def main():
    """Main game loop"""
    global FPS

    # Instantiate the first food object
    food = Food(SCREEN_WIDTH, snake.rect.width)
    food_group.add(food)

    # Set allowed input events
    pygame.event.set_allowed(QUIT)
    pygame.event.set_allowed(KEYDOWN)

    # Play background music
    pygame.mixer.Sound.play(bg_music)

    while True:

        # Check user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check for user keyboard presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if snake.is_alive:
                    if event.key == pygame.K_UP:
                        snake.move_up()
                    elif event.key == pygame.K_DOWN:
                        snake.move_down()
                    elif event.key == pygame.K_LEFT:
                        snake.move_left()
                    elif event.key == pygame.K_RIGHT:
                        snake.move_right()

        # Screen background color
        screen.blit(background, (0, 0))

        # Draw the objects from groups on screen
        food_group.draw(screen)
        snake_group.draw(screen)

        if snake.is_alive:

            # Rotate the snake head depending on direction
            snake.rotate_head()

            # Make body follow the head
            snake.follow_head(snake_group)

            # Check if snake has collided with food
            if food.is_collided(snake):
                # Remove food from ground
                food.remove(food_group)
                # Create new food on a random position
                food = food.create_food(snake_group, food_group, SCREEN_WIDTH, snake.rect.width)
                # Prolong the snake body by 1
                snake.create_new_body(snake_group)
                # Play crunch sound effect
                pygame.mixer.Sound.play(crunch_fx)
                # Increase FPS by 0.25
                FPS += 0.25

            # Move & control the snake head
            snake.update()

            if snake.has_snake_collided_itself(snake_group):
                # Play game over sound effect
                pygame.mixer.Sound.play(game_over_fx)

            # Check for snake wall collision
            if snake.wall_collision(snake.rect.width, SCREEN_WIDTH):
                # Play game over sound effect
                pygame.mixer.Sound.play(game_over_fx)

            pygame.mixer.Sound.play(move_fx)

        # Refresh display on each frame
        pygame.display.update()
        # Set FPS value
        clock.tick(FPS)


main()
pygame.quit()
