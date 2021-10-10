import pygame


class Snake(pygame.sprite.Sprite):
    """A class to manage Snake attributes"""
    def __init__(self, image):
        super(Snake, self).__init__()
        self.image = image.convert_alpha()
        self.reset_image = pygame.image.load("assets/head_brown.png").convert_alpha()
        self.surface = pygame.Surface((30, 30))
        self.rect = self.image.get_rect()
        self.is_moving_up = False
        self.is_moving_down = False
        self.is_moving_right = True
        self.is_moving_left = False
        self.rotation_is_done = False

    def rotate_head(self):
        """Rotate snake snake depending on the move direction"""
        if self.is_moving_right and not self.rotation_is_done:
            self.reset_rotation(90)
        elif self.is_moving_left and not self.rotation_is_done:
            self.reset_rotation(270)
        elif self.is_moving_up and not self.rotation_is_done:
            self.reset_rotation(180)
        elif self.is_moving_down and not self.rotation_is_done:
            self.reset_rotation(0)

    def reset_rotation(self, degree):
        """Reset the snake head rotation to default and
        depending on move direction set a new rotation"""
        self.image = self.reset_image
        self.image = pygame.transform.rotate(self.image, degree)
        self.rotation_is_done = True

    def reset_moving_flags(self):
        """Reset all flag booleans to False"""
        self.is_moving_up = False
        self.is_moving_down = False
        self.is_moving_right = False
        self.is_moving_left = False
        self.rotation_is_done = False

    def update(self):
        # Runs of every frame
        if self.is_moving_up:
            self.rect.top -= 30
        elif self.is_moving_down:
            self.rect.bottom += 30
        elif self.is_moving_left:
            self.rect.left -= 30
        elif self.is_moving_right:
            self.rect.right += 30

    @staticmethod
    def follow_head(group):
        # Make body follow the snake head
        if len(group) > 1:
            i = 2
            x = 1
            # Set the last body part's position in list to the
            # one before it to create the following illusion
            for _ in range(len(group) - 1):
                pos = group.sprites()[-i].rect.center
                group.sprites()[-x].rect.center = pos
                i += 1
                x += 1

    @staticmethod
    def create_new_body(group):
        # Create new snake body part
        body = Snake(pygame.image.load("assets/body_brown.png"))
        body.rect.center = group.sprites()[len(group) - 1].rect.center
        group.add(body)

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
