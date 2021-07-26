from app.contstants import WIN_WIDTH, WIN_HEIGHT
from random import randint

import pygame


class Card:
    __sheet = None
    w, h = (71, 96)

    def __init__(self):
        """Initialize a Card to be moved on the board."""
        self.sprite = pygame.Surface((Card.w, Card.h))
        self.rect = self.sprite.get_rect()

        offset_rect = pygame.Rect(
            Card.w * randint(0, 12), Card.h * randint(0, 3), Card.w, Card.h
        )

        self.sprite.blit(self.sheet, self.rect, offset_rect)

        self.rect.x = WIN_WIDTH if randint(0, 1) else -Card.w
        self.rect.y = randint(-WIN_HEIGHT, WIN_HEIGHT)
        self.invincible_cycles = 10

        self.y_momentum = 0
        self.direction = (1 if randint(0, 1) else -1) * randint(1, 3)
        self.gain = 0.2

    @property
    def sheet(self):
        if self.__sheet is None:
            self.__sheet = pygame.image.load("img/cards.png").convert_alpha()

        return self.__sheet

    def move(self, screen_rect):
        if self.rect.y > WIN_HEIGHT - Card.h:
            self.y_momentum = -self.y_momentum
            self.gain *= randint(1, 2)
        else:
            self.y_momentum += self.gain

        self.rect.x += self.direction
        self.rect.y += self.y_momentum

        if self.invincible_cycles:
            self.invincible_cycles -= 1
            return

        if not self.rect.colliderect(screen_rect) or self.gain > 50:
            self.__init__()

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)
