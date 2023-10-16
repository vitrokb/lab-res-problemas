cards = list(map(int, input().split(" ")))

ascending_cards = cards.copy()
ascending_cards.sort()

descending_cards = cards.copy()
descending_cards.sort(reverse=True)

if cards == ascending_cards:
    print("C")
elif cards == descending_cards:
    print("D")
else:
    print("N")
