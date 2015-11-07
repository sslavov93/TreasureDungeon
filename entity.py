class Entity():
    """Base class. Represents an entity inside the dungeon

    Args:
        name - The name of the Hero entity. Type(String)
        health - The starting health points of the entity. Type(String)"""
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = None
        self.location = None

    def get_health(self):
        """Returns health of the entity (had it not been obvious enough)"""
        return self.health

    def is_alive(self):
        """Returns true if entity's health is above 0"""
        if self.health == 0:
            return False
        return True

    def take_damage(self, damage_points):
        """Reduces entity's health with given damage points

        Args:
            damage_points - Amount of health to be reduced. Type(Integer)"""
        if damage_points > self.health:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        """Increases entity's health with given healing points

        Args:
            healing_points - Amount of health to be increased. Type(integer)"""
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
        """Equips weapon if it's more powerful than the already equipped

        Args:
            weapon - The weapon the entity is wielding. Type(Weapon)"""
        if not self.has_weapon():
            self.weapon = weapon
        elif weapon.damage > self.weapon.damage:
            self.weapon = weapon

    def attack(self):
        """Returns the damage caused by a single hit of the entity

        Damage is calculated by multiplying the entity's
        weapon damage with the chance of a critical hit
        """
        if self.weapon is None:
            return 0
        elif self.weapon.critical_hit():
            return self.weapon.damage * 2
        else:
            return self.weapon.damage
