class Hand:
    def __init__(self):
        self.cards = []
        self.old_card_positions = []

    def add_cards(self, cards):
        if isinstance(cards, list):
            for card in cards:
                self.old_card_positions.append(card.position)
            self.cards += cards
        else:
            self.old_card_positions.append(cards.position)
            self.cards.append(cards)

    def clean(self):
        self.cards.clear()
        self.old_card_positions.clear()

    def reset_cards(self):
        for i in range(len(self.cards)):
            self.cards[i].position = self.old_card_positions[i]
