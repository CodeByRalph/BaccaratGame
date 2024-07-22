import random


def card_value(card):
    if card in ['10', 'J', 'Q', 'K']:
        return 0
    elif card == 'A':
        return 1
    else:
        return int(card)
    

def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    full_deck = cards + cards + cards + cards
    return random.choice(full_deck)


def calculate_points(hand):
    total = sum(card_value(card) for card in hand)
    return total % 10

def player_third_card(hand):
    if calculate_points(hand) <= 5:
        return hand.append(deal_card())


def banker_third_card(banker_hand, player_hand):
    if len(player_hand) == 2:
        if calculate_points(banker_hand) <= 5:
            return banker_hand.append(deal_card())
    else: 
        banker_points = calculate_points(banker_hand)
        if banker_points <= 2:
            return banker_hand.append(deal_card())
        elif banker_points == 3:
            if player_hand[2] in ['2', '3', '4', '5', '6', '7', '9', '10', 'J', 'Q', 'K', 'A']:
                return banker_hand.append(deal_card())
        elif banker_points == 4:
            if player_hand[2] in ['2', '3', '4', '5', '6', '7']:
                return banker_hand.append(deal_card())
        elif banker_points == 5:
            if player_hand[2] in ['4', '5', '6', '7']:
                return banker_hand.append(deal_card())
        elif banker_points == 6:
            if player_hand[2] in ['6', '7']:
                return banker_hand.append(deal_card())   
    
def check_natural(banker_hand, player_hand):
    if calculate_points(banker_hand) == 9 or calculate_points(banker_hand) == 8:
        print('Banker Wins')
        return True
    elif calculate_points(player_hand) == 9 or calculate_points(player_hand) == 8:
        print('Player Wins')
        return True
    else:
        return False

def main():
    player_hand = [deal_card(), deal_card()]
    banker_hand = [deal_card(), deal_card()]

    print(f"Player Hand: {player_hand} -> Points: {calculate_points(player_hand)}")
    print(f"Banker Hand: {banker_hand} -> Points: {calculate_points(banker_hand)}\n")

    win = check_natural(banker_hand, player_hand)
    if not win:
        player_third_card(player_hand)
        banker_third_card(banker_hand, player_hand)
        
        print(f"Player Hand: {player_hand} -> Points: {calculate_points(player_hand)}")
        print(f"Banker Hand: {banker_hand} -> Points: {calculate_points(banker_hand)}")

        if calculate_points(player_hand) > calculate_points(banker_hand):
            print("Player wins")
        elif calculate_points(player_hand) < calculate_points(banker_hand):
            print('Banker Wins')
        else:
            print("Draw")
if __name__ == '__main__':
    main()