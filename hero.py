from entity import Entity


class Hero(Entity):
    """Extends entity class. Represents the human player's 'Hero' character

    Args:
        name - The name of the Hero entity. Type(String)
        health - The starting health points of the entity. Type(String)
        nickname - The nickname of the Hero entity. Type(String)"""
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        self.nickname = nickname

    def known_as(self):
        """Returns the Hero's name and nickname"""
        return "{} the {}".format(self.name, self.nickname)
