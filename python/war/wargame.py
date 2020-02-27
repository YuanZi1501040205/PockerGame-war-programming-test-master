import war

def play_round(deck1: war.Deck, deck2: war.Deck):
        # 1 card compare situation
        if len(deck1.cards) != 0:
            hand_card1 = deck1.draw()
        else:
            deck1.shuffle()
            if len(deck1.cards) != 0: hand_card1 = deck1.draw()
            else: pass
        if len(deck2.cards) != 0:
            hand_card2 = deck2.draw()
        else:
            deck2.shuffle()
            if len(deck1.cards) != 0: hand_card2 = deck2.draw()
            else: pass
        if hand_card1.rank > hand_card2.rank:
            print("Player1 win this round!")
            deck1.discard(card=hand_card1)
            deck2.discard(card=hand_card2)
            play_round(deck1, deck2)
        elif hand_card1.rank == hand_card2.rank:
                fight(deck1, deck2, hand_card1, hand_card2)
        else:
            print("Player2 win this round!")
            deck1.discard(card=hand_card1)
            deck2.discard(card=hand_card2)
            play_round(deck1, deck2)

#players hold one card drawed before move to fight round
def fight(deck1, deck2, hand_card1_0, hand_card2_0):
    hand_card1_1 = None
    hand_card1_2 = None
    hand_card2_1 = None
    hand_card2_2 = None
    #player1 draw cards for fighting
    if len(deck1.cards) >= 2:
        flag1 = 1
        hand_card1_1 = deck1.draw()
        hand_card1_2 = deck1.draw()
        player1_FightCard = hand_card1_2
    elif len(deck1.cards) == 1:
        flag1 = 2
        hand_card1_1 = deck1.draw()
        player1_FightCard = hand_card1_1
    else:
        deck1.shuffle()
        if len(deck1.cards) >= 2:
            flag1 = 3
            hand_card1_1 = deck1.draw()
            hand_card1_2 = deck1.draw()
            player1_FightCard = hand_card1_2
        elif len(deck1.cards) == 1:
            flag1 = 2
            hand_card1_1 = deck1.draw()
            player1_FightCard = hand_card1_1
        else:
            flag1 = 1
            player1_FightCard = hand_card1_0
            pass
    #player2 draw cards for fighting
    if len(deck2.cards) >= 2:
        flag2 = 3
        hand_card2_1 = deck2.draw()
        hand_card2_2 = deck2.draw()
        player2_FightCard = hand_card2_2
    elif len(deck2.cards) == 1:
        flag2 = 2
        hand_card2_1 = deck2.draw()
        player2_FightCard = hand_card2_1
    else:
        deck1.shuffle()
        if len(deck2.cards) >= 2:
            flag2 = 3
            hand_card2_1 = deck2.draw()
            hand_card2_2 = deck2.draw()
            player2_FightCard = hand_card2_2
        elif len(deck2.cards) == 1:
            flag2 = 2
            hand_card2_1 = deck2.draw()
            player2_FightCard = hand_card2_1
        else:
            flag2 = 1
            player2_FightCard = hand_card2_0
            pass

# compare use their most recently drawn card
    if player1_FightCard.rank > player2_FightCard.rank:
        print('player1 win this fight!')
        if flag2 == 3:
            deck1.discard(hand_card2_2)
            deck1.discard(hand_card2_1)
            deck1.discard(hand_card2_0)
        elif flag2 == 2:
            deck1.discard(hand_card2_1)
            deck1.discard(hand_card2_0)
        else:
            deck1.discard(hand_card2_0)
        if deck2.discards != None:
            for var in deck2.discards:
                deck1.discard(var)
            for var in deck2.discards:
                deck2.discards.pop()
        if flag1 == 3:
            deck1.discard(hand_card1_2)
            deck1.discard(hand_card1_1)
            deck1.discard(hand_card1_0)
        elif flag1 == 2:
            deck1.discard(hand_card1_1)
            deck1.discard(hand_card1_0)
        else:
            deck1.discard(hand_card1_0)
        play_round(deck1, deck2)
    elif player1_FightCard.rank == player2_FightCard.rank:
        if flag2 == 3:
            deck1.discard(hand_card2_1)
            deck1.discard(hand_card2_0)
        elif flag2 == 2:
            deck1.discard(hand_card2_0)
        else:
            pass
        if flag1 == 3:
            deck1.discard(hand_card1_1)
            deck1.discard(hand_card1_0)
        elif flag1 == 2:
            deck1.discard(hand_card1_0)
        else:
            pass
        fight(deck1, deck2, player1_FightCard, player1_FightCard)
    else:
        print('player2 win this fight!')
        if flag2 == 3:
            deck2.discard(hand_card1_2)
            deck2.discard(hand_card1_1)
            deck2.discard(hand_card1_0)
        elif flag2 == 2:
            deck2.discard(hand_card1_1)
            deck2.discard(hand_card1_0)
        else:
            deck2.discard(hand_card1_0)
        if deck1.discards != None:
            for var in deck1.discards:
                deck2.discard(var)
            for var in deck1.discards:
                deck1.discards.pop()
        if flag1 == 3:
            deck2.discard(hand_card2_2)
            deck2.discard(hand_card2_1)
            deck2.discard(hand_card2_0)
        elif flag1 == 2:
            deck2.discard(hand_card2_1)
            deck2.discard(hand_card2_0)
        else:
            deck2.discard(hand_card2_0)
        play_round(deck1, deck2)


def play_game(player1: war.Deck, player2: war.Deck):
    """
    This function when called will play an entire game of War.
    playRound will get called until either play is completely out of cards.

    :param player1: Deck of cards representing player 1
    :param player2: Deck of cards representing player 2
    """
    while len(player1) and len(player2):
        play_round(player1, player2)
    if len(player1) == 0:
        print('player2 win this game!')
    else:
        print('player1 win this game!')


def main():
    # Grab a full deck of standard cards and shuffle them.
    deck = war.Deck.create_french_deck(shuffled=True)
    # 'Deal' the deck into two player decks.
    player1 = war.Deck(cards=deck.cards[::2])
    player2 = war.Deck(cards=deck.cards[1::2])
    while len(player1) and len(player2):
        # Play a round.
        play_round(player1, player2)
    if len(player1) == 0:
        print('player2 win this game!')
    else:
        print('player1 win this game!')
        # Play a game.
        # play_game(player1, player2)


if __name__== '__main__':
    main()

