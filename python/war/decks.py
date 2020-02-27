import random
import typing
from war.cards import Card, Suit

Cards = typing.MutableSequence[Card]
OptionalCards = typing.Optional[typing.MutableSequence[Card]]


class Deck:
    def __init__(self, handcards: OptionalCards = None, cards: OptionalCards = None, discards: OptionalCards = None, shuffle: bool = False):
        """
        Creates a deck of cards.

        :param cards: A mutable sequence of cards.  Optional.
        :param discards: A mutable sequence of cards.  Optional.
        :param shuffle: If true, the deck is shuffled immediately after initialization.
        """
        self._cards    = cards or []
        self._discards = discards or []
        if shuffle:
            self.shuffle()

    @property
    def cards(self) -> Cards:
        """
        The cards remaining in the deck from which cards are drawn.

        :return: The deck's cards.
        """
        return self._cards

    @cards.setter
    def cards(self, value: Cards):
        self._cards = value

    @property
    def discards(self) -> Cards:
        """
        The cards that have already been drawn from the deck.

        :return: The deck's discards.
        """
        return self._discards

    @discards.setter
    def discards(self, value: Cards):
        self._discards = value

    def draw(self) -> typing.Optional[Card]:
        """
        Pops the first card in the draw pile sequence.  If empty, returns None.

        :return: A card, or None.
        """
        return self.cards.pop(0) if len(self.cards) else None

    def discard(self, card):
        """
        Discards a card, adding it to the discards.

        :param card: A card.
        """
        self.discards.append(card)

    def shuffle(self):
        """Shuffles the deck."""
        self.cards.extend(self.discards)
        self._discards.clear()
        random.shuffle(self.cards)

    def __eq__(self, other: typing.Any) -> bool:
        return issubclass(type(other), Deck) and self.cards == other.cards and self.discards == other.discards

    def __len__(self) -> int:
        """
        The total number of cards in this deck.

        :return: The deck's card count.
        """
        return len(self.cards) + len(self.discards)

    @staticmethod
    def create_french_deck(shuffled: bool = False):
        """
        Creates a standard deck of thirteen ranks in the French court.  Most common deck used internationally.

        :param shuffled: If true, the deck will be shuffled.
        :return: A french deck.
        """
        return Deck(cards=[Card(rank, suit) for suit in Suit for rank in range(1, 14)], shuffle=shuffled)
