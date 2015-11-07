from entity import Entity


class Orc(Entity):
    """Extends entity class. Represents the computer's 'Orc' NPC character

    Args:
        name - The name of the Orc entity. Type(String)
        health - The starting health points of the Orc entity. Type(String)
        berserk_factor - Damage multiplier coefficient. Type(Double)"""
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = self.set_berserk_factor(berserk_factor)

    def set_berserk_factor(self, berserk):
        """Sets orc's additional damage multiplier

        Args:
            berserk - Orc's damage multiplier. Type(Double)"""
        if float(berserk) < 1.0:
            return 1.0
        elif float(berserk) > 2.0:
            return 2.0
        else:
            return float(berserk)

    def attack(self):
        """Returns the damage caused by a single hit of the orc

        Damage is calculated by multiplying the orc's berserk factor
        with the damage of its weapon and the chance of a critical hit
        """
        if self.weapon is None:
            return 0
        elif self.weapon.critical_hit():
            return self.berserk_factor * self.weapon.damage * 2
        else:
            return self.berserk_factor * self.weapon.damage
