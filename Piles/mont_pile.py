import arcade

class MontPile(arcade.SpriteSolidColor):
    
    def __init__(self, width: int, height: int, color):
        super().__init__(width, height, color)