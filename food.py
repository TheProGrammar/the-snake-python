import pygame
import random


class Food(pygame.sprite.Sprite):
    """A class to manage food attributes."""

    def __init__(self, screen_width, screen_height):
        super(Food, self).__init__()
        self.surface = pygame.Surface((10, 10))
        self.surface.fill('green')
        self.image = self.surface
        self.rect = self.surface.get_rect()
        self.rect.x = random.randrange(self.surface.get_size()[0], screen_width - self.surface.get_size()[0])
        self.rect.y = random.randrange(self.surface.get_size()[0], screen_height - self.surface.get_size()[0])

    def is_collided(self, sprite1):
        """Return true if food collides with the snake"""
        col = pygame.sprite.collide_rect(sprite1, self)
        if col:
            return True

    def remove(self, lst):
        """Empty the food list"""
        lst.empty()

    def create_food(self, lst, width, height):
        """Create food object on random screen position"""
        food = Food(width, height)
        lst.add(food)
        return food
