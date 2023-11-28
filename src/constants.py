import arcade

DISPLAY_SIZE = arcade.get_display_size()

SCREEN_SIZE = {"width": DISPLAY_SIZE[0], "heigth": DISPLAY_SIZE[1]}

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

FACE_DOWN_CARD = ":resources:images/cards/cardBack_red5.png"
CARD_WIDTH = 84
CARD_HEIGTH = 114

CARD_SCALE = (SCREEN_SIZE["heigth"] * 0.1) / CARD_HEIGTH

CARD = {
    "width": CARD_WIDTH * CARD_SCALE,
    "heigth": CARD_HEIGTH * CARD_SCALE,
    "values": [x for x in CARDS.keys()],
    "suits": [x for x in SUITS.keys()],
}


REFRESH_SIZE = 512
REFRESH_SCALE = CARD["heigth"] / REFRESH_SIZE


MAT_PERCENT_OVERSIZE = 2
MAT_HEIGHT = int(CARD["heigth"] * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD["width"] * MAT_PERCENT_OVERSIZE)


VERTICAL_MARGIN_PERCENT = 0.15
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
