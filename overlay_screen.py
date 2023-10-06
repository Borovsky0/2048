import pygame
import constants as c


class OverlayScreen:
    def __init__(
            self, width, height, color, alpha, text, text_color, font, font_size
    ):
        self.font = pygame.font.Font(font, font_size)
        self.text = self.font.render(text, True, text_color)
        self.screen = pygame.Surface((width, height))
        self.screen.set_alpha(alpha)
        self.screen.fill(color)

    def draw(self, screen, center):
        screen.blit(self.screen, (0, 0))
        screen.blit(
            self.text,
            self.text.get_rect(center=center)
        )
