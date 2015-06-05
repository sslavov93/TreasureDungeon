class Entity():
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = None
        self.location = None

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health == 0:
            return False
        return True

    def take_damage(self, damage_points):
        if damage_points > self.health:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        elif self.health + healing_points > self.max_health:
            self.health = self.max_health
        else:
            self.health += healing_points

    def has_weapon(self):
        if self.weapon is not None:
            return True
        return False

    def equip_weapon(self, weapon):
        if not self.has_weapon():
            self.weapon = weapon
        elif weapon.damage > self.weapon.damage:
            self.weapon = weapon

    def attack(self):
        if self.weapon is None:
            return 0
        elif self.weapon.critical_hit():
            return self.weapon.damage * 2
        else:
            return self.weapon.damage
