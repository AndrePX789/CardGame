import arcade

TYPES_PILE = {
    "mont": 0,
    "trash": 1,
    "suits": 2,
    "places": 3
}

class Pile(arcade.SpriteSolidColor):
    
    def __init__(self, width: int, height: int, color, pile_type): 
        super().__init__(width, height, color)