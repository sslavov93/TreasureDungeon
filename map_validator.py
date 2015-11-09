class MapValidator():
    """Base class. Validates user-created map file"""
    def __init__(self):
        pass

    def check_player_spawn(self):
        """Checks whether only one player spawn
        indicator is present on the map"""
        pass

    def check_npc_spawn(self):
        """Checks whether one or more NPC spawn
        indicators are present on the map"""
        pass

    def check_dungeon_dimentions(self):
        """Checks whether the dungeon is a valid square
        (Length is equal to Width)"""
        pass

    def check_key_is_present(self):
        """Checks whether a chest key indicator is present on the map"""
        pass

    def check_chest_is_present(self):
        """Checks whether a chest indicator is present on the map"""
        pass
