import random


class Priesai():
    def __init__(self, health, max_health):
        self.health = health
        self.max_health = max_health

    def get_damaged(self, damage):
        if self.health - damage > 0:
            self.health = self.health - damage
        else:
            self.health = 0
            print("I'm ded")

    def get_recovered(self, heal):
        if self.health + heal > 100:
            self.health = self.max_health
        else:
            self.health = self.health + heal


class Lankininkas(Priesai):
    def __init__(self, health, max_health, dph):
        super().__init__(health, max_health)
        self.dph = dph

    def action(self):
        if self.health >= (20 * self.max_health) / 100:
            print(("Shooting an arrow", self.dph))
            return self.dph
        if self.health < (20 * self.max_health) / 100:
            print("Running away")
            return 0

    def __str__(self):
        return f" Archer -- Health {self.health}/{self.max_health} -- Damage / Hit {self.dph}"


class Riteris(Priesai):
    def __init__(self, health, max_health, dph):
        super().__init__(health, max_health)
        self.dph = dph

    def action(self):
        if self.health == self.max_health:
            print("Charging")
            return 0
        elif self.health >= (10 * self.max_health) / 100:
            print(("Swinging a sword", self.dph))
            return self.dph
        elif self.health < (10 * self.max_health) / 100:
            self.health = self.max_health
            print("Healing myself")
            return 0

    def __str__(self):
        return f" Knight -- Health {self.health}/{self.max_health} -- Damage / Hit {self.dph}"


class Weapon:
    def __init__(self, weapon_name, weapon_dmg):
        self.weapon_name = weapon_name
        self.weapon_dmg = weapon_dmg


class Player(Priesai):
    def __init__(self, health, max_health):
        super().__init__(health, max_health)
        self.weapon = None

    def get_weapon(self, weapon_name, weapon_dmg):
        self.weapon = Weapon(weapon_name, weapon_dmg)

    def action(self):
        print(f"Using a {self.weapon.weapon_name} for {self.weapon.weapon_dmg}")
        return self.weapon.weapon_dmg


class Game:
    def __init__(self, number_of_archers, number_of_knights, player_weapon, player_hp):
        self.number_of_archers = number_of_archers
        self.number_of_knights = number_of_knights
        self.player_weapon = player_weapon
        self.player_hp = player_hp
        self.archers = []
        self.knights = []
        self.player = None

    def set_game(self):
        for archer in range(self.number_of_archers):
            self.archers.append(
                Lankininkas((random.randint(20, 100)), (random.randint(20, 100)), (random.randint(5, 15))))
        for knight in range(self.number_of_knights):
            self.knights.append(Riteris((random.randint(40, 80)), (random.randint(40, 100)), (random.randint(7, 20))))
        self.player = Player(self.player_hp, self.player_hp)
        self.player.get_weapon(self.player_weapon, random.randint(30, 60))

    def turn(self):
        for archer in range(self.number_of_archers):
            print(f"{archer} {self.archers[archer]}")
        for knight in range(self.number_of_knights):
            print(f"{knight} {self.knights[knight]}")
        selection = [input("Attack archer or knight? (type knight/archer) "), int(input("which one? (enter id) "))]
        if selection[0] == "archer":
            self.archers[selection[1]].get_damaged(self.player.action())
        elif selection[0] == "knight":
            self.knights[selection[1]].get_damaged(self.player.action())
        # enemy turn
        for archer in range(self.number_of_archers):
            self.player.get_damaged(self.archers[archer].action())
        for knight in range(self.number_of_knights):
            self.player.get_damaged(self.knights[knight].action())
        if self.player.health <= 0:
            print("game over")
            return False
        else:
            return True


# starting a game

weapon = input("What is your weapon?")
archers = int(input("How many archers will you defeat?  "))
knights = int(input("How many knights will you defeat?   "))
hp = int(input("How healthy are you?"))

game = Game(archers, knights, weapon, hp)
game.set_game()
while True:
    if not game.turn():
        break
