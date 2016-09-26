class Weapon:
    def __init__(self):
        self.damage = 0
        self.durability = 0
    def attack(self):
        self.durability -= 1
        return self.damage

class Sword(Weapon):
    def __init__(self):
        self.damage = 5
        self.durability = 10
