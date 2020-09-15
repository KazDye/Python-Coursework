class Card:

    def __init__(self, suit, face_card):
        self.suit = suit
        self.face_card = face_card

    def get_suit(self):
        color = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        if self.suit is not None:
            try:
                return color[self.suit - 1]
            except IndexError:
                pass
        else:
            pass

    def get_face_card(self):
        cards = [1, 2, 3, 4,
                5, 6, 7, 8,
                9, 10, 11, 12,
                13]
        if self.face_card is not None:
            try:
                return cards[self.face_card - 1]
            except IndexError:
                pass
        else:
            pass

    def get_display_string(self):
        c = self.get_face_card()
        s = self.get_suit()
        if c == 1:
            c = 'Ace'
        elif c == 11:
            c = 'Jack'
        elif c == 12:
            c = 'Queen'
        elif c == 13:
            c = 'King'
        else:
            c = self.get_face_card()
        return '{} of {}'.format(c, s)
