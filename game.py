import arcade
import random
import colors
import constants
from card import Card
from piles import MontPile, TrashPile, PlacesPile, SuitsPile
from hand import Hand


class Solitare(arcade.Window):
    def __init__(self):
        super().__init__(fullscreen=True, title="Solitare")

        self.card_list = None
        self.hand = None
        arcade.set_background_color(colors.PETROLEUM_BLUE)
        self.mont_pile = None
        self.trash_pile = None
        self.suits_piles = None
        self.places_piles = None
        self.is_mont_clicked = False
        self.piles_list = None
        self.current_pile = None

    def setup(self):
        self.hand = Hand()
        self.card_list = arcade.SpriteList()
        self.mont_pile = arcade.SpriteList()
        self.trash_pile = arcade.SpriteList()
        self.suits_piles = arcade.SpriteList()
        self.places_piles = arcade.SpriteList()

        for suit in constants.SUITS.keys():
            for value in constants.CARDS.keys():
                card = Card(value, suit, constants.CARD_SCALE)
                card.position = (constants.START_X, constants.BOTTOM_Y)
                self.card_list.append(card)

        # Shuffle the cards
        for pos1 in range(len(self.card_list)):
            pos2 = random.randrange(len(self.card_list))
            self.card_list.swap(pos1, pos2)

        for i in range(7):
            if i < 2:
                if i == 0:
                    pile = MontPile(constants.MAT_WIDTH, constants.MAT_HEIGHT, colors.BABY_BLUE)
                    pile.position = (
                        constants.START_X + i * constants.X_SPACING,
                        constants.TOP_Y,
                    )
                    self.mont_pile.append(pile)
                else:
                    pile = TrashPile(constants.MAT_WIDTH, constants.MAT_HEIGHT, colors.BABY_BLUE)
                    pile.position = (
                        constants.START_X + i * constants.X_SPACING,
                        constants.TOP_Y,
                    )
                    self.trash_pile.append(pile)
            elif i != 2:
                pile = SuitsPile(constants.MAT_WIDTH, constants.MAT_HEIGHT, colors.BABY_BLUE)
                pile.position = (
                    constants.START_X + i * constants.X_SPACING,
                    constants.TOP_Y,
                )
                self.suits_piles.append(pile)

        for i in range(7):
            pile = PlacesPile(constants.MAT_WIDTH, constants.MAT_HEIGHT, colors.BABY_BLUE)
            pile.position = (
                constants.START_X + i * constants.X_SPACING,
                constants.MIDDLE_Y,
            )
            self.places_piles.append(pile)

        for i, card in enumerate(self.card_list):
            if i < 28:
                for pile in self.places_piles:
                    index = self.places_piles.index(pile)
                    if len(pile.cards) < (index + 1):
                        pile.cards.append(card)
                        break
            else:
                self.mont_pile[0].cards.append(card)
                
        self.piles_list = self.get_all_piles()

    def on_draw(self):
        """Render the screen."""
        # Clear the screen
        self.clear()
        [pile.draw() for pile in self.piles_list]
        self.card_list.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """Called when the user presses a mouse button."""
        cards = arcade.get_sprites_at_point((x, y), self.card_list)
        if arcade.get_sprites_at_point((x, y), self.piles_list):
            self.current_pile = arcade.get_sprites_at_point((x, y), self.piles_list)[0]
        if not cards:
            mont = arcade.get_sprites_at_point((x, y), self.mont_pile)
            if mont:
                mont[0].restart_mont(self.trash_pile[0])
        else:
            first_card = cards[-1]
            if first_card in self.mont_pile[0].cards:
                first_card.face_up()
                self.trash_pile[0].add_card(first_card, self.mont_pile[0])
                first_card.is_just_left_from_mont = True
                self.is_mont_clicked = True
                self.pull_to_top(first_card)
            elif first_card in self.trash_pile[0].cards:
                self.hand.add_cards(first_card)
                self.pull_to_top(first_card)
            else:
                cards = [card for card in cards if not card.is_face_down]
                self.hand.add_cards(cards)
                self.pull_to_top(cards)

            

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if self.is_mont_clicked:
            self.is_mont_clicked = False
            self.trash_pile[0].cards[-1].is_just_left_from_mont = False
            
        if not self.hand.cards:
            return

        pile, distance = arcade.get_closest_sprite(self.hand.cards[0], self.piles_list)
        if pile in self.places_piles:
            for card in self.hand.cards:
                pile.add_card(card, self.current_pile)
        
        reset_position = True
            
        if reset_position:
            self.hand.reset_cards()                
        
        self.hand.clean()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """User moves mouse"""
        # If we are holding cards, move them with the mouse
        for card in self.hand.cards:
            if not card.is_just_left_from_mont:
                card.center_x += dx
                card.center_y += dy

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.close()

    def get_all_piles(self):
        final_list = arcade.SpriteList()
        final_list.extend(self.mont_pile)
        final_list.extend(self.trash_pile)
        final_list.extend(self.suits_piles)
        final_list.extend(self.places_piles)
        return final_list
    
    def pull_to_top(self, cards):
        if isinstance(cards, list):
            for card in cards:
                self.card_list.remove(card)
                self.card_list.append(card)
        else:
            self.card_list.remove(cards)
            self.card_list.append(cards)
def main():
    """Main function"""
    window = Solitare()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
