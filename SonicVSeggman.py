class Battle:
    def __init__(self):
        self.sonic_hp = 100
        self.eggman_hp = 150
    
    def start(self):
        print("⚔️ Sonic vs. Eggman! Press [A]ttack, [S]pin Dash, [H]eal")
        while self.sonic_hp > 0 and self.eggman_hp > 0:
            print(f"Sonic: {self.sonic_hp} HP | Eggman: {self.eggman_hp} HP")
            action = input("Action: ").lower()
            if action == "a":
                self.eggman_hp -= 20
                print("Sonic hits Eggman for 20 damage!")
            elif action == "s":
                self.eggman_hp -= 30
                self.sonic_hp -= 10
                print("Spin Dash! 30 damage (Sonic takes 10 recoil).")
            elif action == "h":
                self.sonic_hp += 25
                print("Sonic healed 25 HP!")
            
            # Eggman's turn
            if self.eggman_hp > 0:
                self.sonic_hp -= 15
                print("Eggman attacks! Sonic loses 15 HP.")
        
        print("You won!" if self.sonic_hp > 0 else "Game Over!")

Battle().start()
