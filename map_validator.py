import os


class MapValidator():
    """Base class. Validates user-created map file"""
    def __init__(self, location):
        self.map_contents = self.read_file(location)
        self.map_length = 0
        self.map_width = 0
        self.player_spawn = False
        self.npc_spawn = False
        self.key_present = False
        self.chest_present = False

    def read_file(self, map_file):
        """Loads dungeon map from specified absolute path in the harddisk

        Args:
            map_file - /full/path/to/map/file.txt"""
        if not os.path.exists(map_file):
            return ''
        with open(map_file, 'r') as f:
            contents = f.read()
        return contents

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
