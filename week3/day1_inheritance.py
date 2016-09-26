class Monster:

    def __init__(self):
        self.hp = 10

class Weapon:
    def __init__(self):
        self.damage = 0
        self.durability = 0
    def attack(self):
        self.set_durability()
        return self.damage
    def set_durability(self):
        self.durability -= 1
        if self.durability < 0:
            self.durability = 0
            self.damage = 0

class Sword(Weapon):
    def __init__(self):
        self.damage = 5
        self.durability = 10

class unbreakableSword(Sword):

    def set_durability(self):
        pass


orc = Monster()
bad_sword = Sword()

orc.hp -= bad_sword.attack()

print(orc.hp)
