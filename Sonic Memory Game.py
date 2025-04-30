import random
cards = ["Sonic", "Tails", "Knuckles", "Eggman"] * 2
random.shuffle(cards)
revealed = [False] * 8

while not all(revealed):
    print("\n" + " ".join([f"{i+1}:{'?' if not revealed[i] else cards[i]}" for i in range(8)]))
    a, b = map(int, input("Pick two cards (1-8): ").split())
    if cards[a-1] == cards[b-1]:
        revealed[a-1] = revealed[b-1] = True
        print("Match!")
    else: print("No match!")

print("You won!")
