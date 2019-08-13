import pygame
import random
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SECOND = 50


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = random.randint(1, 437)

    def update(self):
        self.rect.y += self.speed
