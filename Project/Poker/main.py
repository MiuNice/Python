import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(i) for i in range(3, 11)] + list("JQKA2") + ["joker"]
    suits = "spades diamonds clubs hearts".split()
    suit_val = dict(spades=3, hearts=2, diamonds=1, clubs=0, small=1, big=2)

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits for rank in self.ranks if rank != "joker"] + \
                     [Card("joker", "small"), Card("joker", "big")]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, item):
        return self._card[item]

    def spades_high(self, card):
        return self.ranks.index(card.rank) * (len(self.suit_val) - 2) + self.suit_val[card.suit]

    def sort_french_deck(self, reverse=False):
        return sorted(self, key=self.spades_high, reverse=reverse)


if __name__ == '__main__':
    deck = FrenchDeck()
    print(len(deck))

    card = Card("joker", "big")
    print(FrenchDeck.ranks.index(card.rank))

    print(deck.spades_high(card))

    print(deck.sort_french_deck())
