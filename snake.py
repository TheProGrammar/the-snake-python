import pygame


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super(Snake, self).__init__()
        self.surface = pygame.Surface((25, 25))
        self.color = (255, 255, 255)
        self.surface.fill(self.color)
        self.image = self.surface
        self.rect = self.image.get_rect()

    def set_rounded(self, roundness):
        surface_size = self.surface.get_size()
        self.rect_image = pygame.Surface(surface_size, pygame.SRCALPHA)
        pygame.draw.rect(self.rect_image, self.color, (0, 0, * surface_size), border_radius=roundness)
        self.image = self.surface.copy().convert_alpha()
        self.image.blit(self.rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN)

    def move(self):
        self.rect.x += 1
