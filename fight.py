from random import randint


class Fight():
    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def coin_toss(self):
        coin = randint(1, 10)
        if coin <= 5:
            return (self.hero, self.orc)
        return (self.orc, self.hero)

    def simulate_fight(self):
        if self.hero.weapon is None and self.orc.weapon is None:
            return 'No winner'

        (attacker, defender) = self.coin_toss()

        while self.orc.is_alive() and self.hero.is_alive():
            damage = attacker.attack()
            defender.take_damage(damage)
            attacker, defender = defender, attacker

        if self.hero.is_alive():
            return self.hero
        return self.orc
