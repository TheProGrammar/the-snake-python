import pygame
import random


class Food(pygame.sprite.Sprite):
    """A class to manage food attributes."""

    def __init__(self, screen_width, snake_width):
        super(Food, self).__init__()
        self.surface = pygame.Surface((10, 10))
        self.surface.fill('green')
        self.image = self.surface
        self.rect = self.surface.get_rect()
        self.position_list = []
        self.fill_pos_list(screen_width, snake_width)
        self.rect.x = random.choice(self.position_list)
        self.rect.y = random.choice(self.position_list)

    def fill_pos_list(self, screen_width, snake_width):
        pos = 10
        self.position_list.append(pos)
        for _ in range(int(screen_width / snake_width) - 1):
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

    def create_food(self, lst, width, height, snake_width):
        """Create food object on random screen position"""
        food = Food(width, height, snake_width)
        lst.add(food)
        return food
