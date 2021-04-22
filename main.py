import pygame
from random import randint

clock = pygame.time.Clock()

WIN_WIDTH, WIN_HEIGHT = 1280, 720
icon = pygame.Surface((32, 32), pygame.SRCALPHA)
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen_rect = screen.get_rect()
screen.fill((0, 99, 0))


class Card:
    sheet = pygame.image.load("cards.png").convert()
    w, h = (71, 96)

    def __init__(self):
        self.sprite = pygame.Surface((Card.w, Card.h))
        self.rect = self.sprite.get_rect()

        offset_rect = pygame.Rect(Card.w * randint(0, 12), Card.h * randint(0, 3), Card.w, Card.h)
        self.sprite.blit(Card.sheet, self.rect, offset_rect)

        self.rect.x, self.rect.y = WIN_WIDTH if randint(0, 1) else -Card.w, randint(-WIN_HEIGHT, WIN_HEIGHT)
        self.invincible_cycles = 10

        self.y_momentum = 0
        self.direction = (1 if randint(0, 1) else -1) * randint(1, 3)
        self.gain = 0.2

    def move(self):
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


cards = [Card() for i in range(100)]

is_running = True
while is_running:
    pygame.display.set_caption(f"Solitaire XP Win - By Edhyjox - {clock.get_fps():.0f} Fps")

    for card in cards:
        card.move()
        screen.blit(card.sprite, card.rect)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    clock.tick(60)

pygame.display.quit()
pygame.quit()
