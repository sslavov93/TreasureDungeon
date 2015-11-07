from random import uniform


class Weapon():
    """Base class. Represents the weapon wielded by an entity

    Args:
        type - Player-specified weapon type. Type(String)
        damage - Damage that weapon is causing. Type(Integer)
        critical_percent - Critical strike probability. Type(Double)"""
    def __init__(self, type, damage, critical_percent):
        self.type = type
        self.damage = damage
        self.critical_percent = self.set_critical_percent(critical_percent)

    def set_critical_percent(self, crit):
        """Establishes critical percent multiplier of the weapon

        Args:
            crit - Critical strike probability. Type(Double)"""
        if crit > 1.0:
            return 1.0
        elif crit <= 0:
            return 0.1
        else:
            return crit

    def critical_hit(self):
        """Determines whether the damage would be normal or critical"""
        chance = uniform(0, 1.0)
        if chance <= self.critical_percent:
            return True
        return False
