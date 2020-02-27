package us.knexus.deck;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

/**
 *
 * @author Justin
 */
public class Deck {
    /**
     * The list of cards representing the 'Draw Pile'. Or cards which can be drawn.
     */
    private List<Card> drawPile;
    
    /**
     * The list of cards representing the 'Discard Pile'. Or cards to be shuffled in.
     */
    private List<Card> discardPile;
    
    /**
     * Default Constructor.
     * Creates an empty deck
     */
    public Deck() {
        drawPile = new ArrayList<>();
        discardPile = new ArrayList<>();
    }
    
    /**
     * Constructs a deck with the given List of Card objects. Copies the Cards
     * into the drawPile List
     * 
     * @param cards 
     */
    public Deck(List<Card> cards) {
        drawPile = new ArrayList<>(cards);
        discardPile = new ArrayList<>();
    }
    
    /**
     * Copy Constructor. Creates a new deck with deep copies of the given
     * deck's Draw and Discard pile lists
     * 
     * @param other 
     */
    public Deck(Deck other) {
        drawPile = new ArrayList<>(other.drawPile);
        discardPile = new ArrayList<>(other.discardPile);
    }
    
    /**
     * Removes the first card in the draw pile list and returns it. If
     * draw pile is empty, returns null
     * 
     * @return Card - First card in Draw Pile, null if empty
     */
    public Card draw() {
        if( drawPile.isEmpty() )
            return null;
        return drawPile.remove(0);
    }
    
    /**
     * Adds the given Card to the bottom of the discard pile (back of the
     * discardPile list)
     * 
     * @param card Card - To add to the discard pile
     */
    public void addToDiscard(Card card) {
        discardPile.add(card);
    }
    
    /**
     * Moves all cards from the discard pile to the draw pile and randomizes
     * the draw pile's order.
     */
    public void shuffle() {
        drawPile.addAll(discardPile);
        discardPile.clear();
        
        Collections.shuffle(drawPile);
    }
    
    /**
     * Returns the number of cards currently in the Draw Pile
     * 
     * @return int - Number of cards in drawPile list
     */
    public int getDrawPileSize() {
        return drawPile.size();
    }
    
    /**
     * Returns the number of cards currently in the Discard Pile
     * 
     * @return int - Number of cards in discardPile list
     */
    public int getDiscardPileSize() {
        return discardPile.size();
    }
    
    /**
     * Returns the number of cards currently in the Deck (draw and discard piles)
     * 
     * @return int - Number of cards in any pile of the deck
     */
    public int getNumCards() {
        return drawPile.size() + discardPile.size();
    }

    /**
     * Generated hashCode method.

     * @return int - Hashed representation of a deck
     */
    @Override
    public int hashCode() {
        return Objects.hash(drawPile, discardPile);
    }

    /**
     * Generated equals method.
     *
     * @param o - Object to compare to this
     * @return boolean - Whether or not the given Object is equivalent to this Deck
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Deck deck = (Deck) o;
        return Objects.equals(drawPile, deck.drawPile) &&
            Objects.equals(discardPile, deck.discardPile);
    }

    /**
     * Creates a standard deck of thirteen ranks in the French court.  Most common deck used internationally.
     *  4 of each card 2-10 (one of each suit)
     *  4 of each Jack, Queen, King, and Ace (one of each suit)
     * @return Deck - A full, traditional, 52 card deck in ordinal and suit order
     */
    public static Deck createFullDeck() {
        List<Card> cards = new ArrayList<>();
        for (int rank = 1; rank < 14; ++rank) {
            for (Card.Suit suit : Card.Suit.values()) {
                cards.add(new Card(suit, rank));
            }
        }

        return new Deck(cards);
    }
}
