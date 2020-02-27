
package us.knexus.deck;


import java.util.Objects;

/**
 * @author Justin
 */
public class Card {
    /**
     * An enumeration of possible card suits
     */
    public enum Suit {Club, Diamond, Heart, Spade}

    /**
     * The suit of this card (Club, Diamond, Heart, Spade)
     */
    private final Suit suit;

    /**
     * A numeric representation of the rank of this card.
     * Ace=1, 2-10 for normal cards, Face cards: Jack=11, Queen=12, King=13
     */
    private final int rank;

    /**
     * Card Constructor. Creates a Card with a given Name, Suit and Ordinal.
     * @param suit - The Suit of this card
     * @param rank - A numerical value representing the rank of this card
     */
    public Card(Suit suit, int rank) {
        this.suit = suit;
        this.rank = rank;
    }

    /**
     * The name of this card. (2-10, Jack, Queen, King, Ace)
     * @return name - String name of card
     */
    public String getName() {
        switch (rank) {
            case 11:
                return "Jack";
            case 12:
                return "Queen";
            case 13:
                return "King";
            case 14:
                return "Ace";
            default:
                return String.valueOf(rank);
        }
    }

    /**
     * Gets the suit of this card
     * @return suit - Suit enum value of this card
     */
    public Suit getSuit() {
        return suit;
    }

    /**
     * A numeric representation of the value of this card.
     * @return int - Integer value representation of this card
     */
    public int getOrdinal() {
        return rank == 1 ? 12 : rank - 2;
    }

    /**
     * Gets the rank of this card
     * @return int - Integer value representation of the rank of this card
     */
    public int getRank() {
        return rank;
    }

    /**
     * Pretty prints this card as 'NAME of SUITs' (5 of Clubs, Ace of Spaces, ...)
     * @return String - Pretty printed representation of this card
     */
    @Override
    public String toString() {
        return String.format("%s of %ss", getName(), suit.name());
    }

    /**
     * Generated hashCode method.
     * @return int - Hashed representation of a deck
     */
    @Override
    public int hashCode() {
        return Objects.hash(suit, rank);
    }

    /**
     * Generated equals method.
     * @param o - Object to compare to this
     * @return boolean - Whether or not the given Object is equivalent to this Deck
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Card card = (Card) o;
        return rank == card.rank &&
            suit == card.suit;
    }
}
