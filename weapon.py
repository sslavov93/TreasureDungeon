from random import uniform


class Weapon():
    def __init__(self, type, damage, critical_percent):
        self.type = type
        self.damage = damage
        self.critical_percent = self.set_critical_percent(critical_percent)

    def set_critical_percent(self, crit):
        if crit > 1.0:
            return 1.0
        elif crit <= 0:
            return 0.1
        else:
            return crit

    def critical_hit(self):
        chance = uniform(0, 1.0)
        if chance <= self.critical_percent:
            return True
        return False
