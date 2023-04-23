import arcade
import random
import colors
import constants
from arcade import color as defaul_colors
from card import Card


class Solitare(arcade.Window):
    def __init__(self):
        super().__init__(fullscreen=True, title="Solitare")

        self.card_list = None

        arcade.set_background_color(colors.PETROLEUM_BLUE)

        # List of cards we are dragging with the mouse
        self.held_cards = None

        # Original location of cards we are dragging with the mouse in case
        # they have to go back.
        self.held_cards_original_position = None
        # Sprite list with all the mats tha cards lay on.
        self.pile_mat_list = None
        
        self.piles = None

    def setup(self):
        # List of cards we are dragging with the mouse
        self.held_cards = []

        # Original location of cards we are dragging with the mouse in case
        # they have to go back.
        self.held_cards_original_position = []
        
        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()
        
        for i in range(7):
            if i != 2:
                pile = arcade.SpriteSolidColor(constants.MAT_WIDTH, constants.MAT_HEIGHT, colors.BABY_BLUE)
                pile.position = constants.START_X + i * constants.X_SPACING, constants.TOP_Y
                self.pile_mat_list.append(pile)
            
        for i in range(7):
            pile = arcade.SpriteSolidColor(constants.MAT_WIDTH, constants.MAT_HEIGHT, colors.BABY_BLUE)
            pile.position = constants.START_X + i * constants.X_SPACING, constants.MIDDLE_Y
            self.pile_mat_list.append(pile)
        
        self.card_list = arcade.SpriteList()

        for suit in constants.SUITS.keys():
            for value in constants.CARDS.keys():
                card = Card(value, suit, constants.CARD_SCALE)
                card.position = (constants.START_X, constants.BOTTOM_Y)
                self.card_list.append(card)
        
        # Shuffle the cards
        for pos1 in range(len(self.card_list)):
            pos2 = random.randrange(len(self.card_list))
            self.card_list.swap(pos1, pos2)

    def on_draw(self):
        """Render the screen."""
        # Clear the screen
        self.clear()
        self.pile_mat_list.draw()
        self.card_list.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """Called when the user presses a mouse button."""
        cards = arcade.get_sprites_at_point((x, y), self.card_list)
        
        if len(cards) > 0:

            # Might be a stack of cards, get the top one
            primary_card = cards[-1]

            # All other cases, grab the face-up card we are clicking on
            self.held_cards = [primary_card]
            # Save the position
            self.held_cards_original_position = [self.held_cards[0].position]
            # Put on top in drawing order
            self.pull_to_top(self.held_cards[0])

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        # If we don't have any cards, who cares
        if len(self.held_cards) == 0:
            return

        # Find the closest pile, in case we are in contact with more than one
        pile, distance = arcade.get_closest_sprite(self.held_cards[0], self.pile_mat_list)
        reset_position = True

        # See if we are in contact with the closest pile
        if arcade.check_for_collision(self.held_cards[0], pile):

            # For each held card, move it to the pile we dropped on
            for i, dropped_card in enumerate(self.held_cards):
                # Move cards to proper position
                dropped_card.position = pile.center_x, pile.center_y

            # Success, don't reset position of cards
            reset_position = False

            # Release on top play pile? And only one card held?
        if reset_position:
            # Where-ever we were dropped, it wasn't valid. Reset the each card's position
            # to its original spot.
            for pile_index, card in enumerate(self.held_cards):
                card.position = self.held_cards_original_position[pile_index]
        
        # We are no longer holding cards
        self.held_cards = []

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """User moves mouse"""
         # If we are holding cards, move them with the mouse
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.close()
            
    def pull_to_top(self, card: arcade.Sprite):
        """ Pull card to top of rendering order (last to render, looks on-top) """

        # Remove, and append to the end
        self.card_list.remove(card)
        self.card_list.append(card)


def main():
    """Main function"""
    window = Solitare()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
