from entity import Entity


class Orc(Entity):
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = self.set_berserk_factor(berserk_factor)

    def set_berserk_factor(self, berserk):
        if float(berserk) < 1.0:
            return 1.0
        elif float(berserk) > 2.0:
            return 2.0
        else:
            return float(berserk)

    def attack(self):
        if self.weapon is None:
            return 0
        elif self.weapon.critical_hit():
            return self.berserk_factor * self.weapon.damage * 2
        else:
            return self.berserk_factor * self.weapon.damage
