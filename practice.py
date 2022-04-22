#to shuffle the deck of cards we need to use the shuffle module.
#import the required moodule
#declare a class names Caeds which will have cariables suites and values , now instead of using self. suites and self.values
#we are going to declare them as global variables.
#declare a class deck which will have an empty list named as mycardset. and the suites and values will be appended to mycardset list.
#create popCard()
#import required module
from random import shuffle

#define a class to create
#all type of cards
class Cards:
    global suites, values
    suites = ["Hearts", "Diamonds","Clubs","Spades"]
    values = ["A",'2','3','4','5','6','7','8','9','10','J','Q','K']

    def __init__(self):
        pass
#define a class to catagorize each cards
class Deck(Cards):
    def __init__(self):
        Cards.__init__(self)
        self.mycardset = []
        for n in suites:
            for c in values:
                self.mycardset.append((c)+" "+"of"+" "+n)


#method to remove a card from the deck
def popCard(self):
    if len(self.mycardset) == 0:
        return "NO CARDS CAN BE POPPED FUTHER"
    else:
        cardpopped = self.mycardset.pop()

#define a class gto shuffle the deck of cards
class ShuffleCards(Deck):
    # constructor
    def __init__(self):
        Deck.__init__(self)
    # method to shuffle cards
    def shuffle(self):
        if len(self.mycardset) < 52:
            print("cannot shuffle the cards")
        else:
            shuffle(self.mycardset)
            return self.mycardset
#method to remove a card from the deck
    def popCard(self):
            if len(self.mycardset) == 0:
                return "NO CARDS CAN BE POPPED FURTHER"
            else:
                cardpopped = self.mycardset.pop()
                return (cardpopped)


#deiver code
#ovject create
objCards = Cards()
objDeck = Deck()
#player 1
player1Cards = objDeck.mycardset
print("\n player 1 Cards : \n", player1Cards)
#player2
objShuffleCards = ShuffleCards()
player2Cards = objDeck.mycardset
print("\n player 1 Cards : \n", player2Cards)
#remove some cards
print('\n Removing a card from the Deck:', objShuffleCards.popCard())
print('\n Removing another card from the Deck: ',objShuffleCards.popCards())