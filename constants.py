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

# Styling
CELL_SIZE = 200

NEW_GAME_BUTTON_WIDTH = CELL_SIZE
NEW_GAME_BUTTON_HEIGHT = int(CELL_SIZE / 2)
NEW_GAME_BUTTON_TEXT_FONT_SIZE = int(NEW_GAME_BUTTON_HEIGHT * 0.4)
NEW_GAME_BUTTON_TEXT_FONT_COLOR = "#fcfbf4"

PADDING = int(CELL_SIZE / 7)

BORDER_RADIUS = int(CELL_SIZE / 20)

WINDOW_HEIGHT = CELL_SIZE * 4 + PADDING * 6 + NEW_GAME_BUTTON_HEIGHT
WINDOW_WIDTH = CELL_SIZE * 4 + PADDING * 5

CHECK_SCREEN_ALPHA = 192
CHECK_SCREEN_FONT_SIZE = WINDOW_WIDTH // 10

BACKGROUND_COLOR = "#bbada0"
WIN_SCREEN_COLOR = "#edc22e"
LOSE_SCREEN_COLOR = "#f75f3b"

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
