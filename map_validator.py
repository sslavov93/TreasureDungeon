import os


class MapValidator():

    """Base class. Validates user-created map file"""

    def __init__(self, location):
        self.map = self.read_file(location)
        self.player_spawn = False
        self.npc_spawn = False
        self.key_present = False
        self.chest_present = False
        self.rectangular = False
        self.borders = False

    def read_file(self, map_file):
        """Loads dungeon map from specified absolute path in the harddisk

        Args:
            map_file - /full/path/to/map/file.txt. Type(String)"""
        if not os.path.exists(map_file):
            return ""
        with open(map_file, "r") as f:
            contents = f.read()
        return contents

    def generic_check(self, map_character):
        """Checks whether only a single character
        occurence is present on the map

        Args:
            map_character: The char which occurence would be checked
        """
        count = 0
        for character in self.map:
            if character == map_character:
                count += 1
        if count == 1:
            return True
        return False

    def check_player_spawn(self):
        """Checks whether only one player spawn
        indicator is present on the map"""
        return self.generic_check("S")

    def check_npc_spawn(self):
        """Checks whether one or more NPC spawn
        indicators are present on the map"""
        count = 0
        for character in self.map:
            if character == "N":
                count += 1
        if count != 0:
            return True
        return False

    def check_dungeon_is_rectangular(self):
        """Checks whether the dungeon is a valid square
        (Length is equal to Width)"""
        dims = self.map.split("\n")
        length = len(dims[0])
        for each in dims:
            if len(each) != length:
                return False
        return True

    def check_dungeon_borders(self):
        """Checks whether the outer border of the dungeon
        map consists of 'Z' characters"""
        dims = self.map.split("\n")
        for each in dims[0]:
            if each != "Z":
                return False
        for each in dims[-1]:
            if each != "Z":
                return False
        for each in dims[1:-1]:
            if each[0] != "Z" or each[-1] != "Z":
                return False
        return True

    def check_key_is_present(self):
        """Checks whether a chest key indicator is present on the map"""
        return self.generic_check("K")

    def check_chest_is_present(self):
        """Checks whether a chest indicator is present on the map"""
        return self.generic_check("C")

    def validate_map(self):
        """Utilize all the helper methods to check whether the input map is
        valid and conforms to all the specified conditions."""
        self.npc_spawn = self.check_npc_spawn()
        self.player_spawn = self.check_player_spawn()
        self.key_present = self.check_key_is_present()
        self.chest_present = self.check_chest_is_present()
        self.borders = self.check_dungeon_borders()
        self.rectangular = self.check_dungeon_is_rectangular()
        return (self.player_spawn and self.npc_spawn and self.key_present and
                self.chest_present and self.rectangular and self.borders)

    def generate_message(self):
        """Generate a return message after the map validation process."""
        message = ""
        if (self.player_spawn and self.npc_spawn and self.key_present and
                self.chest_present and self.rectangular and self.borders):
            return "Your map is valid. Dungeon loaded."

        if not self.player_spawn:
            message += "There is an error with the player spawn slots.\n"
        if not self.npc_spawn:
            message += "There is an error with the NPC spawn slots.\n"
        if not self.key_present:
            message += "There is an error with the key slot.\n"
        if not self.chest_present:
            message += "There is an error with the chest slot.\n"
        if not self.rectangular:
            message += "Your dungeon is not rectangular.\n"
        if not self.borders:
            message += "There is an error with the dungeon borders."
        return message
