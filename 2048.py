import pygame
import constants as c
import logic
import button

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(
    (c.WINDOW_WIDTH, c.WINDOW_HEIGHT),
    pygame.RESIZABLE
)
pygame.display.set_caption("AI 2048")
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
    "#fcfbf4",
    c.FONT_NAME,
    int(c.NEW_GAME_BUTTON_HEIGHT / 2)
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
                font = pygame.font.SysFont(
                    c.FONT_NAME,
                    c.FONT_SIZE[matrix[i][j]],
                    bold=True
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
            matrix = logic.game(c.SIZE)

        pygame.display.flip()

        if logic.win(matrix, c.WIN_NUMBER):
            game_done = True


if __name__ == '__main__':
    run()
