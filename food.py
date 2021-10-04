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

    def collision_check(self, sprite1):
        col = pygame.sprite.collide_rect(sprite1, self)
        if col:
            return True
        else:
            return False
