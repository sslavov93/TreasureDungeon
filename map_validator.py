import os


class MapValidator():

    """Base class. Validates user-created map file"""

    def __init__(self, location):
        self.map = self.read_file(location)
        self.map_length = 0
        self.map_width = 0
        self.player_spawn = False
        self.npc_spawn = False
        self.key_present = False
        self.chest_present = False

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
        return (self.check_npc_spawn() and
                self.check_player_spawn() and
                self.check_chest_is_present() and
                self.check_key_is_present() and
                self.check_dungeon_borders() and
                self.check_dungeon_is_rectangular())

# m_starts = "multiple_starts.txt"
# n_starts = "no_start.txt"
# m_chests = "multiple_chests.txt"
# n_chests = "no_chest.txt"
# m_keys = "multiple_keys.txt"
# n_key = "no_keys.txt"
# n_npcs = "no_npcs.txt"
# o_npc = "one_npc.txt"
# rect_c = "rectangle_corr.txt"
# rect_inc = "rectangle_incorr.txt"
# bord_c = "borders_corr.txt"
# bord_inc = "borders_incorr.txt"
# correct = "correct.txt"

# dung = MapValidator("/home/sslavov93/Desktop/invalid_maps/" + m_starts)
# print(dung.validate_map())
# dung = MapValidator("/home/sslavov93/Desktop/invalid_maps/" + n_starts)
# print(dung.validate_map())
# dung = MapValidator("/home/sslavov93/Desktop/invalid_maps/" + m_chests)
# print(dung.validate_map())
# dung = MapValidator("/home/sslavov93/Desktop/invalid_maps/" + n_chests)
# print(dung.validate_map())
# dung = MapValidator("/home/sslavov93/Desktop/invalid_maps/" + m_keys)
# print(dung.validate_map())
# dung = MapValidator("/home/sslavov93/Desktop/invalid_maps/" + n_key)
# print(dung.validate_map())
# dung = MapValidator("/home/sslavov93/Desktop/invalid_maps/" + n_npcs)
# print(dung.validate_map())
# dung = MapValidator("/home/sslavov93/Desktop/invalid_maps/" + rect_inc)
# print(dung.validate_map())
# dung = MapValidator("/home/sslavov93/Desktop/invalid_maps/" + bord_inc)
# print(dung.validate_map())
# dung = MapValidator("/home/sslavov93/Desktop/invalid_maps/" + o_npc)
# print(dung.validate_map())
# dung = MapValidator("/home/sslavov93/Desktop/invalid_maps/" + bord_c)
# print(dung.validate_map())
# dung = MapValidator("/home/sslavov93/Desktop/invalid_maps/" + rect_c)
# print(dung.validate_map())
# dung = MapValidator("/home/sslavov93/Desktop/invalid_maps/" + correct)
# print(dung.check_dungeon_borders())
