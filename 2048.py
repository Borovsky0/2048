import pygame
import os
import platform
import constants as c
from logic import Logic

if platform.system() == 'Windows':
    data_folder = os.path.join(os.getenv('LOCALAPPDATA'), '2048')
elif platform.system() == 'Linux':
    data_folder = os.path.join(os.getenv('HOME'), '2048')

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(
    (c.WINDOW_WIDTH, c.WINDOW_HEIGHT),
    # pygame.RESIZABLE
)
pygame.display.set_caption("2048")
pygame.display.set_icon(pygame.image.load('icon.png'))
clock = pygame.time.Clock()

commands = {
    pygame.K_UP: "up",
    pygame.K_DOWN: "down",
    pygame.K_LEFT: "left",
    pygame.K_RIGHT: "right"
}

score_button_font = pygame.font.Font(
    c.FONT_NAME,
    c.NEW_GAME_BUTTON_TEXT_FONT_SIZE
)


def save_score(score):
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

    with open(os.path.join(data_folder, 'score.bin'), 'wb') as file:
        file.write(score.to_bytes(4, byteorder='big', signed=True))


def load_score():
    try:
        with open(os.path.join(data_folder, 'score.bin'), 'rb') as file:
            return int.from_bytes(file.read(), byteorder='big', signed=True)
    except FileNotFoundError:
        save_score(0)
        return 0


def save_state(matrix, score):
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

    with open(os.path.join(data_folder, 'state.bin'), 'wb') as file:
        for row in matrix:
            for number in row:
                file.write(number.to_bytes(4, byteorder='big', signed=True))

        file.write(score.to_bytes(4, byteorder='big', signed=True))


def load_state():
    game = Logic(c.SIZE)
    score = 0

    try:
        with open(os.path.join(data_folder, 'state.bin'), 'rb') as file:
            for i in range(c.SIZE):
                for j in range(c.SIZE):
                    game.matrix[i][j] = int.from_bytes(file.read(4), byteorder='big', signed=True)
            score = int.from_bytes(file.read(4), byteorder='big', signed=True)
    except FileNotFoundError:
        save_state(game.matrix, score)
        return game.matrix, score
    return game.matrix, score


def draw(matrix, score, highscore):
    # Временно
    # print('Score: ', score)
    # print('Highscore: ', highscore)

    screen.fill(c.BACKGROUND_COLOR)
    x, y = c.PADDING, c.PADDING

    # если кнопка новой игры нажата, то restart = True
    restart = False
    if c.MAIN_NEW_GAME_BUTTON.draw(screen, x, y):
        restart = True

    x += c.CELL_SIZE * 2 + c.PADDING * 2
    c.SCORE_BUTTON.draw(screen, x, y)
    score_button_text = score_button_font.render(
        str(score),
        True,
        c.TEXT_FONT_COLOR
    )
    screen.blit(score_button_text, score_button_text.get_rect(
        center=(x + c.BUTTON_WIDTH / 2, y + (c.BUTTON_HEIGHT / 3) * 2)
    ))

    x += c.PADDING + c.CELL_SIZE
    c.HIGHSCORE_BUTTON.draw(screen, x, y)
    highscore_button_text = score_button_font.render(
        str(highscore),
        True,
        c.TEXT_FONT_COLOR
    )
    screen.blit(highscore_button_text, highscore_button_text.get_rect(
        center=(x + c.BUTTON_WIDTH / 2, y + (c.BUTTON_HEIGHT / 3) * 2)
    ))

    y += c.PADDING + c.BUTTON_HEIGHT
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
    highscore = load_score()

    game = Logic(c.SIZE)

    game.load(*load_state())

    game_done = False

    while not game_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_state(game.matrix, game.score)
                game_done = True
            if event.type == pygame.KEYDOWN:
                if event.key in commands:
                    done = getattr(game, commands[event.key])()
                    if done:
                        game.add()
                        if game.score > highscore:
                            highscore = game.score
                            save_score(highscore)

        if draw(game.matrix, game.score, highscore):
            c.CHECK_SCREEN.draw(
                screen,
                (c.WINDOW_WIDTH / 2, c.WINDOW_HEIGHT / 2)
            )

            c.YES_BUTTON.draw(
                screen,
                c.PADDING * 2 + c.CELL_SIZE,
                c.WINDOW_HEIGHT / 2 + c.OVERLAY_SCREEN_FONT_SIZE
            )

            c.NO_BUTTON.draw(
                screen,
                c.PADDING * 3 + c.CELL_SIZE * 2,
                c.WINDOW_HEIGHT / 2 + c.OVERLAY_SCREEN_FONT_SIZE
            )
            pygame.display.flip()

            check_screen_is_on = True
            while check_screen_is_on:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        check_screen_is_on = False
                        game_done = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if c.YES_BUTTON.rect.collidepoint(event.pos):
                            game = Logic(c.SIZE)
                            check_screen_is_on = False
                        if c.NO_BUTTON.rect.collidepoint(event.pos):
                            check_screen_is_on = False

        pygame.display.flip()
        clock.tick(c.FPS)

        if game.win(c.WIN_NUMBER):
            c.WIN_SCREEN.draw(
                screen,
                (c.WINDOW_WIDTH / 2, c.WINDOW_HEIGHT / 2)
            )

            c.WIN_SCREEN_NEW_GAME_BUTTON.draw(
                screen,
                c.PADDING * 2.5 + c.CELL_SIZE * 1.5,
                c.WINDOW_HEIGHT / 2 + c.OVERLAY_SCREEN_FONT_SIZE
            )
            pygame.display.flip()

            win_screen_is_on = True
            while win_screen_is_on:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        win_screen_is_on = False
                        game_done = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if c.WIN_SCREEN_NEW_GAME_BUTTON.rect.collidepoint(event.pos):
                            game = Logic(c.SIZE)
                            win_screen_is_on = False

        if not game.game_not_over():
            c.LOSE_SCREEN.draw(
                screen,
                (c.WINDOW_WIDTH / 2, c.WINDOW_HEIGHT / 2)
            )

            c.LOSE_SCREEN_NEW_GAME_BUTTON.draw(
                screen,
                c.PADDING * 2.5 + c.CELL_SIZE * 1.5,
                c.WINDOW_HEIGHT / 2 + c.OVERLAY_SCREEN_FONT_SIZE
            )
            pygame.display.flip()

            lose_screen_is_on = True
            while lose_screen_is_on:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        lose_screen_is_on = False
                        game_done = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if c.LOSE_SCREEN_NEW_GAME_BUTTON.rect.collidepoint(event.pos):
                            game = Logic(c.SIZE)
                            lose_screen_is_on = False


if __name__ == '__main__':
    run()
