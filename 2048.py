import pygame
import constants as c
from logic import Logic

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(
    (c.WINDOW_WIDTH, c.WINDOW_HEIGHT),
    # pygame.RESIZABLE
)
pygame.display.set_caption("2048")
clock = pygame.time.Clock()

'''
commands = {
    pygame.K_UP: game.up,
    pygame.K_DOWN: game.down,
    pygame.K_LEFT: game.left,
    pygame.K_RIGHT: game.right
}
'''


def draw(matrix, score):
    # Временно
    print(score)

    screen.fill(c.BACKGROUND_COLOR)
    x, y = c.PADDING, c.PADDING

    # если кнопка новой игры нажата, то restart = True
    restart = False
    if c.MAIN_NEW_GAME_BUTTON.draw(screen, x, y):
        restart = True

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
    game = Logic(c.SIZE)
    game_done = False

    while not game_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    done = game.up()
                    if done:
                        game.add()
                elif event.key == pygame.K_DOWN:
                    done = game.down()
                    if done:
                        game.add()
                elif event.key == pygame.K_LEFT:
                    done = game.left()
                    if done:
                        game.left()
                elif event.key == pygame.K_RIGHT:
                    done = game.right()
                    if done:
                        game.add()

        if draw(game.matrix, game.score):
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
