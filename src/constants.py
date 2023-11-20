from win32api import GetSystemMetrics

SCREEN_SIZE = {"width": GetSystemMetrics(0), "heigth": GetSystemMetrics(1)}


SUITS = {"Clubs": "Black", "Spades": "Black", "Hearts": "Red", "Diamonds": "Red"}

CARDS = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
}

FACE_DOWN_IMAGE = ":resources:images/cards/cardBack_red2.png"

CARD_SCALE = 0.7

CARD = {
    "width": 140 * CARD_SCALE,
    "heigth": 190 * CARD_SCALE,
    "values": [x for x in CARDS.keys()],
    "suits": [x for x in SUITS.keys()],
}

MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(CARD["heigth"] * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD["width"] * MAT_PERCENT_OVERSIZE)

VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.15

# The Y of the bottom row (2 piles)
BOTTOM_Y = SCREEN_SIZE["heigth"] - (
    MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT
)

# The X of where to start putting things on the left side
START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

# The Y of the top row (4 piles)
TOP_Y = SCREEN_SIZE["heigth"] - MAT_HEIGHT / 2 - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The Y of the middle row (7 piles)
MIDDLE_Y = TOP_Y - MAT_HEIGHT - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# How far apart each pile goes
X_SPACING = (MAT_WIDTH + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT) + SCREEN_SIZE[
    "width"
] * 0.05

CARD_VERTICAL_OFFSET = CARD["heigth"] * CARD_SCALE * 0.3
