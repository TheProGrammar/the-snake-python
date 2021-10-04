import pygame


class Snake(pygame.sprite.Sprite):
    """A class to manage Snake attributes"""
    def __init__(self):
        super(Snake, self).__init__()
        self.surface = pygame.Surface((30, 30))
        self.color = (255, 255, 255)
        self.surface.fill(self.color)
        self.image = self.surface
        self.rect = self.image.get_rect()
        self.is_moving_up = False
        self.is_moving_down = False
        self.is_moving_right = True
        self.is_moving_left = False

    def set_rounded(self, roundness):
        """Make snake rect with round edges"""
        surface_size = self.surface.get_size()
        self.rect_image = pygame.Surface(surface_size, pygame.SRCALPHA)
        pygame.draw.rect(self.rect_image, self.color, (0, 0, surface_size[0], surface_size[1]), border_radius=roundness)
        self.image = self.surface.copy().convert_alpha()
        self.image.blit(self.rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)

    def reset_moving_flags(self):
        """Reset all moving booleans to False"""
        self.is_moving_up = False
        self.is_moving_down = False
        self.is_moving_right = False
        self.is_moving_left = False

    def update(self):
        if self.is_moving_up:
            self.rect.y -= 30
        elif self.is_moving_down:
            self.rect.y += 30
        elif self.is_moving_left:
            self.rect.x -= 30
        elif self.is_moving_right:
            self.rect.x += 30

    def move_up(self):
        if self.is_moving_down:
            return
        self.reset_moving_flags()
        self.is_moving_up = True

    def move_down(self):
        if self.is_moving_up:
            return
        self.reset_moving_flags()
        self.is_moving_down = True

    def move_left(self):
        if self.is_moving_right:
            return
        self.reset_moving_flags()
        self.is_moving_left = True

    def move_right(self):
        if self.is_moving_left:
            return
        self.reset_moving_flags()
        self.is_moving_right = True
