import random
from dataclasses import dataclass

@dataclass
class Planet:
    name: str
    tech_level: int
    resources: list

@dataclass
class Item:
    name: str
    base_price: int
    tech_level: int

items = [
    Item("Water", 10, 0),
    Item("Ore", 25, 1),
    Item("Medicine", 100, 3),
    Item("AI Cores", 500, 5)
]

planets = [
    Planet("Earth", 3, ["Water", "Medicine"]),
    Planet("Mars", 2, ["Ore"]),
    Planet("Alpha Centauri", 4, ["AI Cores"]),
    Planet("Tau Ceti", 1, ["Water", "Ore"])
]

class Player:
    def __init__(self):
        self.credits = 1000
        self.ship = {"cargo": [], "capacity": 10}
        self.location = planets[0]

def generate_prices(planet):
    prices = {}
    for item in items:
        if item.name in planet.resources:
            price = item.base_price * 0.8
        else:
            price = item.base_price * (1 + (item.tech_level - planet.tech_level) * 0.2)
        prices[item.name] = max(5, int(price * random.uniform(0.9, 1.1)))
    return prices

def travel(player):
    print("\nAvailable planets:")
    for i, planet in enumerate(planets):
        print(f"{i+1}. {planet.name} (Tech: {planet.tech_level})")
    
    choice = int(input("Where to? ")) - 1
    if 0 <= choice < len(planets):
        player.location = planets[choice]
        print(f"\nArrived at {player.location.name}!")
    else:
        print("Invalid choice")

def trade(player):
    prices = generate_prices(player.location)
    
    print("\nMarket Prices:")
    for item, price in prices.items():
        print(f"{item}: {price} credits")
    
    print("\nYour cargo:")
    for item in player.ship["cargo"]:
        print(f"- {item}")
    
    action = input("\n(B)uy or (S)ell? ").lower()
    if action == 'b':
        item = input("What to buy? ")
        if item in prices and len(player.ship["cargo"]) < player.ship["capacity"]:
            if player.credits >= prices[item]:
                player.credits -= prices[item]
                player.ship["cargo"].append(item)
                print(f"Bought {item}!")
            else:
                print("Not enough credits")
        else:
            print("Can't buy that")
    elif action == 's':
        item = input("What to sell? ")
        if item in player.ship["cargo"]:
            player.credits += prices[item]
            player.ship["cargo"].remove(item)
            print(f"Sold {item}!")
        else:
            print("Don't have that")

def main():
    player = Player()
    while True:
        print(f"\n=== {player.location.name} ===")
        print(f"Credits: {player.credits}")
        print(f"Cargo: {len(player.ship['cargo'])}/{player.ship['capacity']}")
        
        action = input("\n(T)ravel, (M)arket, (Q)uit? ").lower()
        if action == 't':
            travel(player)
        elif action == 'm':
            trade(player)
        elif action == 'q':
            break

if __name__ == "__main__":
    main()
