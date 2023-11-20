import arcade
import constants

TYPES_PILE = {"mont": 0, "trash": 1, "suits": 2, "places": 3}


class BasePile(arcade.SpriteSolidColor):
    def __init__(self, width: int, height: int, color):
        super().__init__(width, height, color)

        self.cards = arcade.SpriteList()

    def add_card(self, card: arcade.Sprite, old_pile):
        self.cards.append(card)
        old_pile.cards.remove(card)


class MontPile(BasePile):
    def __init__(self, width: int, height: int, color):
        super().__init__(width, height, color)

    def restart_mont(self, trash_pile: BasePile):
        for card in trash_pile.cards:
            self.add_card(card)

        trash_pile.reset_trash()


class PlacesPile(BasePile):
    def __init__(self, width: int, height: int, color):
        super().__init__(width, height, color)

    def _turn_last_card(self):
        self.cards[-1].face_up()

    def adjust_position_cards(self):
        for i, card in enumerate(self.cards):
            card.position = self.position[0], self.position[1] - (
                constants.CARD_VERTICAL_OFFSET * i
            )

        self._turn_last_card()

    def draw(self):
        self.adjust_position_cards()
        return super().draw()


class SuitsPile(BasePile):
    def __init__(self, width: int, height: int, color):
        super().__init__(width, height, color)


class TrashPile(BasePile):
    def __init__(self, width: int, height: int, color):
        super().__init__(width, height, color)

    def add_card(self, card: arcade.Sprite, mont_pile: BasePile):
        card.position = self.position
        return super().add_card(card, mont_pile)

    def reset_trash(self):
        self.cards.clear()
