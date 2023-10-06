import pygame
import constants as c
import logic
import button

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(
    (c.WINDOW_WIDTH, c.WINDOW_HEIGHT),
)
pygame.display.set_caption("2048")
clock = pygame.time.Clock()

commands = {
    pygame.K_UP: logic.up,
    pygame.K_DOWN: logic.down,
    pygame.K_LEFT: logic.left,
    pygame.K_RIGHT: logic.right
}

new_game_button = button.Button(
    c.NEW_GAME_BUTTON_WIDTH,
    c.NEW_GAME_BUTTON_HEIGHT,
    c.CELL_COLOR[0],
    "NEW GAME",
    c.NEW_GAME_BUTTON_TEXT_FONT_COLOR,
    c.FONT_NAME,
    c.NEW_GAME_BUTTON_TEXT_FONT_SIZE,
    button.ButtonTextLayout.column
)

yes_button = button.Button(
    c.NEW_GAME_BUTTON_WIDTH,
    c.NEW_GAME_BUTTON_HEIGHT,
    c.CELL_COLOR[0],
    "YES",
    c.NEW_GAME_BUTTON_TEXT_FONT_COLOR,
    c.FONT_NAME,
    c.NEW_GAME_BUTTON_TEXT_FONT_SIZE,
)

no_button = button.Button(
    c.NEW_GAME_BUTTON_WIDTH,
    c.NEW_GAME_BUTTON_HEIGHT,
    c.CELL_COLOR[0],
    "NO",
    c.NEW_GAME_BUTTON_TEXT_FONT_COLOR,
    c.FONT_NAME,
    c.NEW_GAME_BUTTON_TEXT_FONT_SIZE,
)


def draw(matrix):
    screen.fill(c.BACKGROUND_COLOR)

    x, y = c.PADDING, c.PADDING

    # если кнопка новой игры нажата, то restart = True
    restart = False
    if new_game_button.draw(screen, x, y):
        restart = True

    y += c.PADDING + c.NEW_GAME_BUTTON_HEIGHT
    for i in range(len(matrix)):
        x = c.PADDING
        for j in range(len(matrix)):
            pygame.draw.rect(
                screen,
                c.CELL_COLOR[matrix[i][j]],
                (x, y, c.CELL_SIZE, c.CELL_SIZE),
                border_radius=c.BORDER_RADIUS
            )

            if matrix[i][j]:
                font = pygame.font.Font(
                    c.FONT_NAME,
                    c.FONT_SIZE[matrix[i][j]],
                )

                text = font.render(
                    str(matrix[i][j]),
                    True,
                    c.TEXT_COLOR[matrix[i][j]]
                )

                screen.blit(text, text.get_rect(
                    center=(x + c.CELL_SIZE / 2, y + c.CELL_SIZE / 2)
                ))
            x += c.PADDING + c.CELL_SIZE
        y += c.PADDING + c.CELL_SIZE

    return restart


def run():
    matrix = logic.game(c.SIZE)
    game_done = False

    while not game_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_done = True
            if event.type == pygame.KEYDOWN:
                if event.key in commands:
                    matrix, done = commands[event.key](matrix)
                    if done:
                        matrix = logic.add(matrix)

        if draw(matrix):
            check_screen = pygame.Surface(
                (c.WINDOW_WIDTH, c.WINDOW_HEIGHT),
            )
            # устанавливаем прозрачность
            check_screen.set_alpha(c.CHECK_SCREEN_ALPHA)
            check_screen.fill(c.BACKGROUND_COLOR)
            screen.blit(check_screen, (0, 0))

            check_screen_font = pygame.font.Font(
                c.FONT_NAME, c.CHECK_SCREEN_FONT_SIZE
            )
            check_screen_text = check_screen_font.render(
                "ARE YOU SURE?",
                True,
                c.NEW_GAME_BUTTON_TEXT_FONT_COLOR
            )
            screen.blit(
                check_screen_text,
                check_screen_text.get_rect(
                    center=(c.WINDOW_WIDTH / 2, c.WINDOW_HEIGHT / 2)
                )
            )

            yes_button.draw(
                screen,
                c.PADDING * 2 + c.CELL_SIZE,
                c.WINDOW_HEIGHT / 2 + c.CHECK_SCREEN_FONT_SIZE
            )

            no_button.draw(
                screen,
                c.PADDING * 3 + c.CELL_SIZE * 2,
                c.WINDOW_HEIGHT / 2 + c.CHECK_SCREEN_FONT_SIZE
            )
            pygame.display.flip()

            win_screen_is_on = True
            while win_screen_is_on:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        win_screen_is_on = False
                        game_done = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if yes_button.rect.collidepoint(event.pos):
                            matrix = logic.game(c.SIZE)
                            win_screen_is_on = False
                        if no_button.rect.collidepoint(event.pos):
                            win_screen_is_on = False

        pygame.display.flip()

        if logic.win(matrix, c.WIN_NUMBER):
            game_done = True


if __name__ == '__main__':
    run()
