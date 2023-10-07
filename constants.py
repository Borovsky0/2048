import button
import overlay_screen

# Game data
SIZE = 4
WIN_NUMBER = 2048

POWERS = {
    2:      1,
    4:      2,
    8:      3,
    16:     4,
    32:     5,
    64:     6,
    128:    7,
    256:    8,
    512:    9,
    1024:   10,
    2048:   11
}

CELL_COLOR = {
    0:      "#cdc1b4",
    2:      "#eee4da",
    4:      "#eee1c9",
    8:      "#f3b27a",
    16:     "#f69664",
    32:     "#f77c5f",
    64:     "#f75f3b",
    128:    "#eed072",
    256:    "#edcc62",
    512:    "#edc850",
    1024:   "#edc53f",
    2048:   "#edc22e"
}

# Styling
CELL_SIZE = 150

BUTTON_WIDTH = CELL_SIZE
BUTTON_HEIGHT = int(CELL_SIZE / 2)
BUTTON_COLOR = CELL_COLOR[0]
NEW_GAME_BUTTON_TEXT_FONT_SIZE = int(BUTTON_HEIGHT * 0.40)
TEXT_FONT_COLOR = "#fcfbf4"

PADDING = int(CELL_SIZE / 7)

BORDER_RADIUS = int(CELL_SIZE / 20)

WINDOW_HEIGHT = CELL_SIZE * 4 + PADDING * 6 + BUTTON_HEIGHT
WINDOW_WIDTH = CELL_SIZE * 4 + PADDING * 5

OVERLAY_SCREEN_ALPHA = 192
OVERLAY_SCREEN_FONT_SIZE = WINDOW_WIDTH // 10

BACKGROUND_COLOR = "#bbada0"
WIN_SCREEN_COLOR = "#edc22e"
LOSE_SCREEN_COLOR = "#f75f3b"


TEXT_COLOR = {
    2:      "#776e65",
    4:      "#776e65",
    8:      "#f9f6f2",
    16:     "#f9f6f2",
    32:     "#f9f6f2",
    64:     "#f9f6f2",
    128:    "#f9f6f2",
    256:    "#f9f6f2",
    512:    "#f9f6f2",
    1024:   "#f9f6f2",
    2048:   "#f9f6f2"
}

FONT_NAME = "fonts/tahomabd.ttf"

FONT_SIZE = {
    2:      int(CELL_SIZE / 2),
    4:      int(CELL_SIZE / 2),
    8:      int(CELL_SIZE / 2),
    16:     int(CELL_SIZE / 2),
    32:     int(CELL_SIZE / 2),
    64:     int(CELL_SIZE / 2),
    128:    int(CELL_SIZE / 2.5),
    256:    int(CELL_SIZE / 2.5),
    512:    int(CELL_SIZE / 2.5),
    1024:   int(CELL_SIZE / 3),
    2048:   int(CELL_SIZE / 3)
}

FPS = 60

CHECK_SCREEN = overlay_screen.OverlayScreen(
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    BACKGROUND_COLOR,
    OVERLAY_SCREEN_ALPHA,
    "ARE YOU SURE?",
    TEXT_FONT_COLOR,
    FONT_NAME,
    OVERLAY_SCREEN_FONT_SIZE
)

LOSE_SCREEN = overlay_screen.OverlayScreen(
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    LOSE_SCREEN_COLOR,
    OVERLAY_SCREEN_ALPHA,
    "GAME OVER!",
    TEXT_FONT_COLOR,
    FONT_NAME,
    OVERLAY_SCREEN_FONT_SIZE
)

WIN_SCREEN = overlay_screen.OverlayScreen(
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WIN_SCREEN_COLOR,
    OVERLAY_SCREEN_ALPHA,
    "YOU WIN!",
    TEXT_FONT_COLOR,
    FONT_NAME,
    OVERLAY_SCREEN_FONT_SIZE
)

MAIN_NEW_GAME_BUTTON = button.Button(
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_COLOR,
    "NEW GAME",
    TEXT_FONT_COLOR,
    FONT_NAME,
    NEW_GAME_BUTTON_TEXT_FONT_SIZE,
    button.ButtonTextLayout.column
)

YES_BUTTON = button.Button(
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_COLOR,
    "YES",
    TEXT_FONT_COLOR,
    FONT_NAME,
    NEW_GAME_BUTTON_TEXT_FONT_SIZE,
)

NO_BUTTON = button.Button(
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_COLOR,
    "NO",
    TEXT_FONT_COLOR,
    FONT_NAME,
    NEW_GAME_BUTTON_TEXT_FONT_SIZE,
)

WIN_SCREEN_NEW_GAME_BUTTON = button.Button(
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_COLOR,
    "NEW GAME",
    TEXT_FONT_COLOR,
    FONT_NAME,
    NEW_GAME_BUTTON_TEXT_FONT_SIZE,
    button.ButtonTextLayout.column
)

LOSE_SCREEN_NEW_GAME_BUTTON = button.Button(
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_COLOR,
    "NEW GAME",
    TEXT_FONT_COLOR,
    FONT_NAME,
    NEW_GAME_BUTTON_TEXT_FONT_SIZE,
    button.ButtonTextLayout.column
)

SCORE_BUTTON_FONT_SIZE = int(BUTTON_HEIGHT * 0.2)

SCORE_BUTTON = button.Button(
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_COLOR,
    "SCORE",
    "#EEE1C9",
    FONT_NAME,
    SCORE_BUTTON_FONT_SIZE,
    button.ButtonTextLayout.on_top,
    clickable=False
)

HIGHSCORE_BUTTON = button.Button(
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_COLOR,
    "BEST",
    "#EEE1C9",
    FONT_NAME,
    SCORE_BUTTON_FONT_SIZE,
    button.ButtonTextLayout.on_top,
    clickable=False
)
