import random

suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
hand = []
dealer_hand = []
card = ""
dealer_total = 0
player_total = 0
card_val = 0
def deal_Card():

    # globalise player total, so it can be used to track the value of the players hand
    global player_total

    # Randomise card's suit
    card_suit = suits[random.randint(0, 3)]

    # Randomise card's rank
    card_num = ranks[random.randint(0, 12)]

    # If the cards rank is A, J, K, Q, assign a numeric value
    if card_num == "A":
        card_val = 11
    elif card_num == "Jack" or card_num == "Queen" or card_num == "King":
        card_val = 10
    else:
        card_val = card_num

    # add the rank and suit to make a card string
    card = (str(card_num) + " " + str(card_suit))

    # add the card to the players hand
    hand.append(card)
    player_total += card_val

def dealers_Card():

    # globalise player total, so it can be used to track the value of the players hand
    global dealer_total
    # globalise Ace boolean to use later to say whether its val is 1 or 11
    global Ace
    # Randomise card's suit
    card_suit = suits[random.randint(0, 3)]

    # Randomise card's rank
    card_num = ranks[random.randint(0, 12)]

    # If the cards rank is A, J, K, Q, assign a numeric value
    if card_num == "A":
        card_val = 11
        Ace = True
    elif card_num == "Jack" or card_num == "Queen" or card_num == "King":
        card_val = 10
    else:
        card_val = card_num

    # add the rank and suit to make a card string
    card = (str(card_num) + " " + str(card_suit))

    # add the card to the players hand
    dealer_hand.append(card)
    dealer_total += card_val

# initiates player bankroll
bankroll = 100
play_again = "y"

# while loop asks the user if they want to play again
while play_again == "y" and bankroll > 0:

    # deals the dealers first card
    dealers_Card()

    # deals the players first two cards
    deal_Card()
    deal_Card()

    # introduces the player to the game and asks them to place a bet
    print("Welcome to blackjack you cards are: " + str(hand))
    print("The dealer has: " + str(dealer_hand))
    print("Your bank-roll is: £" + str(bankroll))
    bet = input("How much would you like to bet? £")
    bet = int(bet)

    # asks the player to hit or stand
    print("if you would like to hit enter 'h' to stand press 's'")
    ans = input()

    # initiates the game so when the players cards go over 21 or stand the game stops
    while ans == "h" and player_total < 21:
        deal_Card()
        if player_total >= 21:
            break
        print("Your cards are: " + str(hand))
        print("Would you like to hit 'h' or stand 's'?")
        ans = input()
    # plays the dealers second card and prints the hand
    dealers_Card()
    print("The dealer has" + str(dealer_hand))

    # The dealer plays cards until above the players value or bust
    while dealer_total < 21 or dealer_total < player_total:
        if dealer_total < player_total and dealer_total < 21:
            dealers_Card()
        else:
            break

    print(dealer_hand)

    # decides who wins based off end value
    if dealer_total > player_total and dealer_total <= 21:
        print("The dealer wins")
        bankroll -= bet
    elif dealer_total == player_total:
        print("This hand is a draw")
    elif dealer_total < player_total and player_total <= 21:
        print("You Win!")
        bankroll = bankroll + 1.5 * bet
    print("Would you like to play again? 'y' or 'n'")

    # resets the players card values to start another hand
    player_total = 0
    dealer_total = 0
    hand = []
    dealer_hand = []
    play_again = input()

# exit message
if bankroll <= 0:
    print("Unlucky you've gone bust")
elif bankroll < 100:
    print("You didnt lose everything you still have £" + str(bankroll))
else:
    print("You managed to beat the house! you've got £" + str(bankroll))