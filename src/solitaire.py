import arcade
import random
from src.colors import *
from src.constants import *
from src.sprites.card import Card
from src.sprites.refresh import Refresh
from src.hand import Hand
from src.sprites.piles import *
from typing import List


class Solitaire(arcade.Window):
    def __init__(self):
        super().__init__(fullscreen=True, title="Solitarie")
        arcade.set_background_color(PETROLEUM_BLUE)
        self.card_list = None
        self.hand = None
        self.mont_pile = None
        self.trash_pile = None
        self.suits_piles = None
        self.places_piles = None
        self.piles_list = None
        self.current_pile = None
        self.refresh = None

    def setup(self):
        self.hand = Hand()
        self.card_list = arcade.SpriteList()
        self.suits_piles = arcade.SpriteList()
        self.places_piles = arcade.SpriteList()
        self.piles_list = arcade.SpriteList()

        for suit in SUITS.keys():
            for value in CARDS.keys():
                card = Card(value, suit, CARD_SCALE)
                card.position = (START_X, BOTTOM_Y)
                self.card_list.append(card)

        for pos1 in range(len(self.card_list)):
            pos2 = random.randrange(len(self.card_list))
            self.card_list.swap(pos1, pos2)

        for i in range(7):
            if i < 2:
                if i == 0:
                    self.mont_pile = MontPile(MAT_WIDTH, MAT_HEIGHT, BABY_BLUE)
                    self.mont_pile.position = (
                        START_X + i * X_SPACING,
                        TOP_Y,
                    )
                    self.piles_list.append(self.mont_pile)
                else:
                    self.trash_pile = TrashPile(MAT_WIDTH, MAT_HEIGHT, BABY_BLUE)
                    self.trash_pile.position = (
                        START_X + i * X_SPACING,
                        TOP_Y,
                    )
                    self.piles_list.append(self.trash_pile)
            elif i != 2:
                pile = SuitsPile(MAT_WIDTH, MAT_HEIGHT, BABY_BLUE)
                pile.position = (
                    START_X + i * X_SPACING,
                    TOP_Y,
                )
                self.suits_piles.append(pile)

        for i in range(7):
            pile = PlacesPile(MAT_WIDTH, MAT_HEIGHT, BABY_BLUE)
            pile.position = (
                START_X + i * X_SPACING,
                MIDDLE_Y,
            )
            self.places_piles.append(pile)

        self.piles_list.extend(self.places_piles)
        self.piles_list.extend(self.suits_piles)

        for i, card in enumerate(self.card_list):
            if i < 28:
                for pile in self.places_piles:
                    index = self.places_piles.index(pile)
                    if len(pile.cards) < (index + 1):
                        pile.cards.append(card)
                        break
            else:
                self.mont_pile.cards.append(card)

        self.refresh = Refresh(scale=REFRESH_SCALE)
        self.refresh.position = self.mont_pile.position

    def on_draw(self):
        self.clear()
        [pile.draw() for pile in self.piles_list]
        self.card_list.draw()
        self.refresh.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.close()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        cards: List[Card] = arcade.get_sprites_at_point((x, y), self.card_list)
        self.current_pile = None

        piles = arcade.get_sprites_at_point((x, y), self.piles_list)
        if piles:
            self.current_pile = piles[0]

        if cards:
            first_card = cards[-1]
            if isinstance(self.current_pile, MontPile):
                first_card.face_up()
                self.trash_pile.add_card(first_card, self.current_pile)
                self._pull_to_top(first_card)
                if len(self.mont_pile.cards) == 0:
                    self.refresh.visibility(True)
            else:
                self.hand.add_cards(first_card)
                self._pull_to_top(self.hand.cards)
        else:
            if isinstance(self.current_pile, MontPile):
                if len(self.mont_pile.cards) == 0:
                    self.mont_pile.restart_mont(self.trash_pile)
                    self.refresh.visibility(False)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        for card in self.hand.cards:
            card.center_x += dx
            card.center_y += dy

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.hand.clean()

    def _pull_to_top(self, cards):
        if isinstance(cards, list):
            for card in cards:
                self.card_list.remove(card)
                self.card_list.append(card)
        else:
            self.card_list.remove(cards)
            self.card_list.append(cards)
