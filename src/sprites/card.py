from src.constants import SUITS, CARDS, FACE_DOWN_CARD
import arcade


class Card(arcade.Sprite):
    def __init__(self, card: str, suit: str, scale: float = 1) -> None:
        self.card = card
        self.suit = suit
        self._color = SUITS[suit]
        self._value = CARDS[self.card]
        self.image_file_name = f":resources:images/cards/card{self.suit}{self.card}.png"
        self.is_just_left_from_mont = False
        self.is_face_up = False

        super().__init__(FACE_DOWN_CARD, scale, hit_box_algorithm="None")

    def _get_hl(self):
        if self.value == 1:
            return {"high": self.value + 1, "low": None}
        elif self.value == 13:
            return {"high": None, "low": self.value - 1}
        else:
            return {"high": self.value + 1, "low": self.value - 1}

    def face_down(self):
        """Turn card face-down"""
        self.texture = arcade.load_texture(FACE_DOWN_CARD)
        self.is_face_up = False

    def face_up(self):
        """Turn card face-up"""
        self.texture = arcade.load_texture(self.image_file_name)
        self.is_face_up = True

    @property
    def is_face_down(self):
        """Is this card face down?"""
        return not self.is_face_up

    @property
    def color(self):
        return self._color

    @property
    def value(self):
        return self._value

    @property
    def top_down(self):
        return self._get_hl()
