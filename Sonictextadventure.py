import random
import time

class SonicTextAdventure:
    def __init__(self):
        self.rings = 0
        self.chaos_emeralds = 0
        self.game_over = False

    def start(self):
        print("⚡ Sonic Text Adventure ⚡")
        print("Collect rings and Chaos Emeralds to stop Eggman!")
        time.sleep(1)
        self.name = input("Enter your name (or 'Sonic'): ").strip() or "Sonic"
        print(f"\nGo, {self.name}! Eggman's robots are attacking!")
        self.game_loop()

    def game_loop(self):
        actions = ["run", "jump", "spin", "search", "quit"]
        while not self.game_over:
            print(f"\nRings: {self.rings} | Emeralds: {self.chaos_emeralds}/7")
            action = input(f"What will {self.name} do? {actions}: ").lower()
            
            if action not in actions:
                print("Invalid action!")
                continue
            
            if action == "quit":
                self.game_over = True
                print("Gotta go fast... another time!")
                break
            
            self.handle_action(action)
            self.check_win()

    def handle_action(self, action):
        if action == "run":
            print(f"{self.name} dashes through Green Hill Zone!")
            if random.random() < 0.3:
                rings_found = random.randint(1, 10)
                self.rings += rings_found
                print(f"Found {rings_found} rings!")
        
        elif action == "jump":
            enemy = random.choice(["Moto Bug", "Crabmeat", "Buzz Bomber"])
            print(f"{self.name} jumps over a {enemy}!")
        
        elif action == "spin":
            print(f"{self.name} spin-dashes through enemies!")
            self.rings += random.randint(5, 15)
        
        elif action == "search":
            if random.random() < 0.1 and self.chaos_emeralds < 7:
                self.chaos_emeralds += 1
                print(f"⭐ Found a Chaos Emerald! ({self.chaos_emeralds}/7)")
            else:
                print("Nothing here...")

    def check_win(self):
        if self.chaos_emeralds >= 7:
            print("\n🌟 YOU WIN! All Chaos Emeralds collected!")
            print(f"{self.name} transforms into Super Sonic and defeats Eggman!")
            self.game_over = True

if __name__ == "__main__":
    game = SonicTextAdventure()
    game.start()
