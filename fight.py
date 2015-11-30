from random import randint


class Fight():
    """Base class. Represents the encounter of a
    'Hero' with an 'Orc' inside the dungeon

    Args:
        hero - A Hero entity. Type(Hero(Entity))
        orc - An Orc entity. Type(Orc(Entity))"""
    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def coin_toss(self):
        """Helper method. Determines the first entity to attack"""
        coin = randint(1, 10)
        if coin <= 5:
            return (self.hero, self.orc)
        return (self.orc, self.hero)

    def simulate_fight(self):
        """Simulates fight between the two entities and determines a winner"""
        if self.hero.weapon is None and self.orc.weapon is None:
            return "No winner"

        (attacker, defender) = self.coin_toss()

        while self.orc.is_alive() and self.hero.is_alive():
            damage = attacker.attack()
            defender.take_damage(damage)
            attacker, defender = defender, attacker

        if self.hero.is_alive():
            return self.hero
        return self.orc
