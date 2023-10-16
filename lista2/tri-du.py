initial_cards = list(map(int, input().split(" ")))

if initial_cards[0] == initial_cards[1]:
    print(initial_cards[0])
elif initial_cards[0] > initial_cards[1]:
    print(initial_cards[0])
else:
    print(initial_cards[1])
