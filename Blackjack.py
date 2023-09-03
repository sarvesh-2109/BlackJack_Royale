import random
from art import logo
from replit2 import clear


def deal_card():
    """Returns a card at random from the deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score and computer and returns the result."""
    if u_score == c_score:
        return "Draw 😶‍🌫️"
    elif c_score == 0:
        return "You lose. The computer has BlackJack 😭"
    elif u_score == 0:
        return "You win. You have secured a blackjack 🏆"
    elif u_score > 21:
        return "You lose. You went over 😭"
    elif c_score > 21:
        return "You win. The computer went over 🏆"
    elif u_score > c_score:
        return "You win 🏆"
    else:
        return "You lose 😭"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            is_game_over = True
        else:
            new_round = input("Do you wish to draw another card? Type 'y' for yes and 'n' for no:\n").lower()
            if new_round == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack?: Type 'y' or 'n': ").lower() == "y":
    clear()
    play_game()
