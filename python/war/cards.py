# %%
import enum
import typing


class Suit(enum.IntEnum):
    Clubs    = enum.auto()
    Diamonds = enum.auto()
    Hearts   = enum.auto()
    Spades   = enum.auto()


class Card:
    def __init__(self, rank: int, suit: Suit):
        """
        A basic playing card object.

        :param rank: The standardized rank representation of the card.  See Card.__rank_names for name override mapping.
        :param suit: The enumerated suit of this card.
        """
        self._rank = rank
        self._suit = suit

    @property
    def name(self) -> str:
        """
        The name of the card, as determined by the card's ordinal.

        :return: The card's name.
        """
        return Card.__rank_names.get(self._rank, str(self._rank))

    @property
    def suit(self) -> Suit:
        """
        The suit of the card, as per the Suit enumeration.

        :return: The card's suit.
        """
        return self._suit

    @suit.setter
    def suit(self, value: Suit):
        self._suit = value

    @property
    def rank(self) -> int:
        """
        The standardized numeric representation of the card.

        :return: The card's rank.
        """
        return self._rank

    @rank.setter
    def rank(self, value: int):
        self._rank = value

    @property
    def ordinal(self) -> int:
        """
        The value of the card.

        :return: The card's ordinal.
        """
        return self.rank - 2 if self.rank != 1 else 12

    def __hash__(self) -> int:
        return hash((self.suit, self.rank))

    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, Card) and self.suit is other.suit and self.rank == other.rank

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        """
        Pretty prints this card as 'NAME of SUIT' (5 of Clubs, Ace of Spades, ...)

        :return: Pretty printed representation of this card.
        """
        return f'{self.name} of {self.suit.name}'

    __rank_names = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
# %%