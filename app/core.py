from app.contstants import WIN_WIDTH, WIN_HEIGHT
from app.card import Card
import pygame


class App:

    def __init__(self):
        self.is_running = False
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.screen_rect = self.screen.get_rect()

        icon = pygame.Surface((32, 32), pygame.SRCALPHA)
        pygame.display.set_icon(icon)

        self.cards = [Card() for _ in range(100)]

    def run(self):
        self.is_running = True
        self.screen.fill((0, 99, 0))

        while self.is_running:
            pygame.display.set_caption(
                f"Solitaire XP Win - {self.clock.get_fps():.0f} Fps"
            )

            for card in self.cards:
                card.move(self.screen_rect)
                card.draw(self.screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            self.clock.tick(60)

    def __del__(self):
        pygame.display.quit()
        pygame.quit()
