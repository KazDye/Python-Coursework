import random
from cards import Card

def create_deck():
    # The deck array-list will contain Cards
    deck = []

    # Build the deck, assuming the Card class was imported correctly
    for i in range(1, 4+1):
        for j in range(1, 13+1):
            deck.append(Card(i,j))

    return deck

def main():
    print ("The dealer opens a new pack of playing cards.")
    my_deck = create_deck()
    print ("The dealer shuffles.")
    random.shuffle(my_deck)
    print ("The dealer pulls five cards from the top.")
    print ("And we see...")
    for c in my_deck[:5]:
        print ('\t' + c.get_display_string())


if __name__ == "__main__":
    # execute only if run as a script
    main()
