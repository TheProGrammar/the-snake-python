import pygame
import random


class Food(pygame.sprite.Sprite):
    """A class to manage food attributes."""
    def __init__(self, screen_width, snake_width):
        super(Food, self).__init__()
        self.image = pygame.image.load("assets/apple.png")
        self.rect = self.image.get_rect()
        self.position_list = [snake_width]
        self.fill_pos_list(screen_width, snake_width)
        self.rect.x = random.choice(self.position_list)
        self.rect.y = random.choice(self.position_list)

    def fill_pos_list(self, screen_width, snake_width):
        # Fill the position list with possible food locations on ground
        pos = snake_width
        for _ in range(int(screen_width / snake_width) - 2):
            pos += snake_width
            self.position_list.append(pos)

    def is_collided(self, sprite1):
        """Return true if food collides with the snake"""
        col = pygame.sprite.collide_rect(sprite1, self)
        if col:
            return True

    def remove(self, lst):
        """Empty the food list"""
        lst.empty()

    def create_food(self, lst, width, snake_width):
        """Create food object on random screen position"""
        food = Food(width, snake_width)
        lst.add(food)
        return food
