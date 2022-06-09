def BlackjackHighest(hand):
    cards = {
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "jack": 10.1,
        "queen": 10.2,
        "king": 10.3,
        "ace": 11
    }

    cards_keys = list(cards.keys())
    cards_values = list(cards.values())

    hand_total = 0
    card_values_in_hand = []

    for i in hand:
        hand_total += int(cards[i])
        card_values_in_hand.append(cards[i])

    card_values_in_hand.sort()

    ace_count = hand.count("ace")
    for i in range(ace_count):
        if hand_total > 21:
            card_values_in_hand.pop()
            hand_total -= 10

    x = card_values_in_hand[-1]
    position = cards_values.index(x)

    if hand_total < 21:
        return "below " + cards_keys[position]
    elif hand_total > 21:
        return "above " + cards_keys[position]
    else:
        return "blackjack " + cards_keys[position]