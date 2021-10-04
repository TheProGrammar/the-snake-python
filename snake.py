import pygame


class Snake(pygame.sprite.Sprite):
    """A class to manage Snake attributes"""

    def __init__(self, name):
        super(Snake, self).__init__()
        self.surface = pygame.Surface((30, 30))
        self.color = (255, 255, 255)
        self.surface.fill(self.color)
        self.image = self.surface
        self.rect = self.image.get_rect()
        self.name = ""
        self.moving_up = False
        self.moving_down = False
        self.moving_right = True
        self.moving_left = False

    def set_rounded(self, roundness):
        surface_size = self.surface.get_size()
        self.rect_image = pygame.Surface(surface_size, pygame.SRCALPHA)
        pygame.draw.rect(self.rect_image, self.color, (0, 0, surface_size[0], surface_size[1]), border_radius=roundness)
        self.image = self.surface.copy().convert_alpha()
        self.image.blit(self.rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)

    def reset_moving_flags(self):
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_up:
            self.rect.y -= 30
        elif self.moving_down:
            self.rect.y += 30
        elif self.moving_left:
            self.rect.x -= 30
        elif self.moving_right:
            self.rect.x += 30
