import constants as c
import pygame


class Button:
    def __init__(self, width, height, button_color, text, text_color, font, font_size):
        self.width = width
        self.height = height
        self.color = button_color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.font_size = font_size
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.clicked = False

    def draw(self, screen, x, y):
        # если кнопка нажата, то action = True
        action = False

        # обновляем левый верхний угол прямоугольника кнопки
        self.rect.topleft = (x, y)

        # если курсор мыши наведен на кнопку и нажата левая кнопка мыши
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True

        # сбросим клик, если мышь отпущена
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        pygame.draw.rect(
            screen,
            self.color,
            self.rect,
            border_radius=c.BORDER_RADIUS
        )

        font = pygame.font.SysFont(
            self.font,
            self.font_size,
            bold=True
        )

        text = font.render(
            self.text,
            True,
            self.text_color
        )

        screen.blit(text, text.get_rect(
            center=(x + self.width / 2, y + self.height / 2)
        ))

        return action
