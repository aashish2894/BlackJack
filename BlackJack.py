# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
outcome2 = ""
score = 0
state = 0
wins = 0
loses = 0
flag = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.list = []  # create Hand object

    def __str__(self):
        self.ans = ""
        for i in range(len(self.list)):
            self.ans = self.ans + " " + str(self.list[i]) 
        return "Hand contains" + self.ans     # return a string representation of a hand

    def add_card(self, card):
        self.list.append(card)  # add a card object to a hand 

    def get_value(self):
        self.flag = 0
        self.sum = 0
        for i in range(len(self.list)):
            self.sum += VALUES[self.list[i].get_rank()]
            if self.list[i].get_rank() == 'A':
                self.flag = 1
        if self.flag == 0 :
            return self.sum
        else:
            if (self.sum+10)<=21:
                return (self.sum+10)
            else:
                return self.sum
        
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for i in range(len(self.list)):
            self.list[i].draw(canvas,[pos[0]+100*i, pos[1]])
            # draw a hand on the canvas, use the draw method for cards
        
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.c1 = []
        self.list = []
        for i in SUITS:
            for j in RANKS:
                self.list.append(Card(i,j))
            # create a Deck object

    def shuffle(self):
        self.list.extend(self.c1)
        self.c1 = []
        random.shuffle(self.list)
        
        # add cards back to deck and shuffle
            # use random.shuffle() to shuffle the deck

    def deal_card(self):
        self.c2 = self.list.pop()
        self.c1.append(self.c2)
        return self.c2
            # deal a card object from the deck
    
    def __str__(self):
        self.ans = ""
        for i in range(len(self.list)):
            self.ans = self.ans + " " + str(self.list[i])
        return "Deck contains" + self.ans
        


play_deck = Deck()
new_player = Hand()
dealer = Hand()
#define event handlers for buttons
def deal():
    global outcome, in_play,new_player,play_deck,dealer,outcome2,state,wins,loses,flag
    flag = 1
    if in_play == False:
        play_deck.shuffle()
        new_player = Hand()
        dealer = Hand()
        p1 = play_deck.deal_card()
        new_player.add_card(p1)
        d1 = play_deck.deal_card()
        dealer.add_card(d1)
        p2 = play_deck.deal_card()
        new_player.add_card(p2)
        d2 = play_deck.deal_card()
        dealer.add_card(d2)
        #print "Player " + str(new_player)
        #print "Dealer " + str(dealer)
        outcome = "Hit or Stand?"
        in_play = True
        outcome2 = ""
        #print "Player ",new_player.get_value()
        #print "Dealer ",new_player.get_value()
        state = 1
    else :
        outcome2 = "You lose"
        outcome = "New deal?"
        in_play = False
        state = 0
        loses += 1

def hit():
    global outcome,outcome2,state,in_play,wins,loses
    if state == 1:
        p = play_deck.deal_card()
        new_player.add_card(p)
        if new_player.get_value()>21:
            outcome2 = "You went bust and lose"
            outcome = "New deal?"
            state = 0
            in_play = False
            loses += 1
        # replace with your code below
    else :
        pass
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome,outcome2,state,in_play,wins,loses
    in_play = False
    if state == 1:
        if new_player.get_value()>21:
            outcome2 = "You went bust and lose"
            outcome = "New deal?"
            state = 0
            loses += 1
        else:
            while dealer.get_value()<17:
                d = play_deck.deal_card()
                dealer.add_card(d)
            if dealer.get_value()>21:
                outcome2 = "Dealer busts. You win"
                outcome = "New deal?"
                state = 0
                wins += 1
            elif dealer.get_value()>=new_player.get_value():
                outcome2 = "You lose"
                outcome = "New deal?"
                state = 0
                loses += 1
            else :
                outcome2 = "You win"
                outcome = "New deal?"
                state = 0
                wins += 1
    else :
        pass
        # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    if flag == 1:
        canvas.draw_text("Dealer",[50,120],32,"Red")
        canvas.draw_text("Player",[50,320],32,"Red")
        canvas.draw_text("BlackJack",[50,50],32,"DarkOrange")
        canvas.draw_text("Wins = "+str(wins),[300,50],32,"White")
        canvas.draw_text("Loses = "+str(loses),[450,50],32,"White")
        new_player.draw(canvas,[50,350])
        dealer.draw(canvas,[50,150])
        if in_play==True:
            canvas.draw_image(card_back,CARD_BACK_CENTER,CARD_BACK_SIZE,[86.5,199],CARD_SIZE)
        else :
            dealer.draw(canvas,[50,150])
        canvas.draw_text(outcome,[300,320],32,"Black")
        canvas.draw_text(outcome2,[300,120],32,"Black")
    else :
        canvas.draw_text("BlackJack",[50,100],62,"DarkOrange")
        canvas.draw_text("Click deal to start game",[50,200],50,"Black")
    
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# remember to review the gradic rubric