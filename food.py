import pygame
import random


class Food(pygame.sprite.Sprite):
    """A class to manage food attributes."""
    def __init__(self, screen_width, snake_width):
        super(Food, self).__init__()
        self.image = pygame.image.load("assets/images/apple_red.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.position_list = [snake_width]
        self.fill_pos_list(screen_width, snake_width)
        self.rect.x = random.choice(self.position_list)
        self.rect.y = random.choice(self.position_list)

    def fill_pos_list(self, screen_width, snake_width):
        # Fill the position list with possible food locations on ground
        pos = snake_width
        # Fills the list with the positions within the wall
        for _ in range(int(screen_width / snake_width) - 3):
            pos += snake_width
            self.position_list.append(pos)

    def is_collided(self, sprite1):
        """Return true if food collides with the snake"""
        return pygame.sprite.collide_rect(sprite1, self)

    def remove(self, lst):
        """Empty the food list"""
        lst.empty()

    @staticmethod
    def create_food(snake_parts, food_list, screen_width, snake_width):
        """Create food object on random screen position"""
        food = Food(screen_width, snake_width)
        # Prevents food to spawn below the snake's body
        for body in snake_parts:
            while body.rect.center == food.rect.center:
                food = Food(screen_width, snake_width)
        food_list.add(food)
        return food
