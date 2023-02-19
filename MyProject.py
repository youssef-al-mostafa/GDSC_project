import random

def play_game():
    print("Hello, welcome to the youssef Poker game!")
    deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] * 4
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_card = random.choice(deck)
        computer_card = random.choice(deck)
        user_cards.append(user_card)
        computer_cards.append(computer_card)
        deck.remove(user_card)
        deck.remove(computer_card)
    print("Your cards:", user_cards)
    print("Computer's cards:", [computer_cards[0], '?'])
    user_score = sum([10 if card in ['J', 'Q', 'K'] else card for card in user_cards])
    computer_score = sum([10 if card in ['J', 'Q', 'K'] else card for card in computer_cards])
    if user_score == 21:
        print("You have a blackjack! You win.")
    elif computer_score == 21:
        print("Computer has a blackjack. You lose.")
        print("Computer's cards:", computer_cards)
    else:
        while user_score > 21 and 'A' in user_cards:
            user_score -= 10
            user_cards[user_cards.index('A')] = 1
        if user_score > 21:
            print("You bust. You lose.")
        else:
            while input("Do you want to draw another card? (y/n): ").lower() == 'y':
                user_card = random.choice(deck)
                user_cards.append(user_card)
                deck.remove(user_card)
                user_score += (10 if user_card in ['J', 'Q', 'K'] else user_card)
                print("Your cards:", user_cards)
                if user_score > 21:
                    print("You bust. You lose.")
                    print("Computer's cards:", computer_cards)
                    break
            while computer_score < 17:
                computer_card = random.choice(deck)
                computer_cards.append(computer_card)
                deck.remove(computer_card)
                computer_score += (10 if computer_card in ['J', 'Q', 'K'] else computer_card)
            while computer_score > 21 and 'A' in computer_cards:
                computer_score -= 10
                computer_cards[computer_cards.index('A')] = 1
            if computer_score > 21:
                print("Computer bust. You win.")
                print("Computer's cards:", computer_cards)
            else:
                if user_score > computer_score:
                    print("Your score is higher than computer's score. You win.")
                    print("Computer's cards:", computer_cards)
                elif user_score < computer_score:
                    print("Computer's score is higher than your score. You lose.")
                    print("Computer's cards:", computer_cards)
                else:
                    print("It's a draw.")
                    print("Computer's cards:", computer_cards)

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("See you!")

play_game()
