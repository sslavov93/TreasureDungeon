import os
from orc import Orc
from hero import Hero
from weapon import Weapon
from fight import Fight
from random import randint


class Dungeon():
    """Base class. Represents the dungeon in
    which the player would start the game

    Args:
        map - /full/path/to/map/file.txt"""
    def __init__(self, map):
        self.map = self.load_map(map)
        self.ingame = {}
        self.npcs = {}
        self.key_obtained = False
        self.unlocked = False

    def load_map(self, map_file):
        """Loads dungeon map from specified absolute path in the harddisk

        Args:
            map_file - /full/path/to/map/file.txt"""
        if not os.path.exists(map_file):
            return ''
        with open(map_file, 'r') as f:
            contents = f.read()
        return contents

    def print_map(self):
        """Returns current loaded dungeon map"""
        if not self.map:
            return 'No valid map loaded.'
        return self.map

    def convert_map_to_changeable_tiles(self):
        """Helper method. Converts a single string
        to list of lists of strings"""
        new_map = []
        for item in self.map.split():
            new_map.append(list(item))
        return new_map

    def revert_map_to_string_state(self, custom_map):
        """Helper method. Converts list of lists of strings
        to a single string

        Args:
            custom_map - List of lists of strings,
                representing the currently loaded Dungeon map"""
        string_map = ''
        for item in custom_map:
            for char in item:
                string_map += char
            string_map += '\n'
        return string_map[:-1]

    def get_entity_indicator(self, entity):
        """Helper method. Returns the indicator of the current busy entity

        Args:
            entity - Entity object with indicator to be fetched. Type(Orc/Hero)

        'H' - Hero
        'O' - Orc"""
        entities = ['O', 'H']
        if isinstance(entity, Orc):
            return entities[0]
        elif isinstance(entity, Hero):
            return entities[1]
        else:
            return ''

    def get_position_in_map(self, ind):
        """Returns the 2-D coordinates of the specified entity indicator

        Args:
            ind - Indicator of current entity. Type(String)"""
        output = self.convert_map_to_changeable_tiles()
        for row in range(0, len(output)):
            for col in range(0, len(output[0])):
                if output[row][col] == ind:
                    return [row, col]

    def spawn(self, player_name, entity):
        """Spawns a new Hero into the Dungeon field

        Args:
            player_name - The name that represents the Hero character
                on the Dungeon map. Type(String). This is decided by the player
            entity - The object that represents the Hero. Type(Hero(Entity))"""
        if player_name in self.ingame:
            return 'Character is already spawned.'
        indicator = self.get_player_indicator(entity)
        if 'S' in self.map and indicator:
            self.ingame[player_name] = entity
            entity.location = self.get_position_in_map('S')
            self.map = (self.map[:self.map.find('S')] + indicator +
                        self.map[self.map.find('S') + 1:])
        else:
            return 'No free spawn slot.'

    def spawn_npcs(self):
        """Spawns NPCs into the Dungeon field"""
        free_spaces = True
        counter = 1
        while free_spaces:
            if 'N' in self.map:
                npc = Orc('NPC' + str(counter), 250, 1.4)
                wep = Weapon('Axe' + str(counter), 15, 0.7)
                npc.weapon = wep
                self.npcs[npc.name] = npc
                self.ingame[npc.name] = npc
                npc.location = self.get_position_in_map('N')
                self.map = (self.map[:self.map.find('N')] + 'O' +
                            self.map[self.map.find('N') + 1:])
                counter += 1
            else:
                free_spaces = False

    def get_destination_coordinates(self, current_location, direction):
        """Get the coordinates of the direction
            in which an entity decides to move

        Args:
            current_location - Current coordinates of entity. Type(Tuple)
            direction - One of 'left', 'right', 'up', 'down'. Type(String)
        """
        current = current_location[:]
        if direction == "up":
            current[0] -= 1
        if direction == "down":
            current[0] += 1
        if direction == "left":
            current[1] -= 1
        if direction == "right":
            current[1] += 1
        return current

    def check_move(self, target, direction):
        """Check if desired move is valid

        Args:
            target - The entity that will be performing the move
            direction - The direction in terms of the dungeon realm
                (available directions - 'left', 'right', 'up', 'down')

        Map Legend:
        # - Dungeon wall
        Z - Dungeon boundary
        """
        directions = ['left', 'right', 'up', 'down']
        if direction not in directions:
            # print("Wrong direction given.")
            return False
        if target == "#":
            # print("You will hit the wall.")
            return False
        if target == 'Z':
            # print('Out of bounds.')
            return False
        return True

    def regular_move(self, name, dest, otpt, chr_loc):
        """Perform a regular move

        Args:
            name - Name of the Entity that would move. Type(String)
            dest - Coordinates of move direction. Type(Tuple)
            otpt - Converted map. Type(List of Lists of Strings)
            chr_loc - Current coordinates of entity. Type(Tuple)"""
        self.ingame[name].location = dest
        otpt[chr_loc[0]][chr_loc[1]], otpt[dest[0]][dest[1]] = otpt[
            dest[0]][dest[1]], otpt[chr_loc[0]][chr_loc[1]]
        self.map = self.revert_map_to_string_state(otpt)
        return 'Successful Move.'

    def obtain_key(self, name, dest, otpt, chr_loc):
        """Get key that unlocks chest (and ultimately wins the game)

        Args:
            name - Name of the Entity that gets the key. Type(String)
            dest - Coordinates of the key. Type(Tuple)
            otpt - Converted map. Type(List of Lists of Strings)
            chr_loc - Current coordinates of Entity. Type(Tuple)"""
        self.ingame[name].location = dest
        otpt[chr_loc[0]][chr_loc[1]], otpt[dest[0]][dest[1]] = otpt[
            dest[0]][dest[1]], otpt[chr_loc[0]][chr_loc[1]]
        self.map = self.revert_map_to_string_state(otpt)
        self.map = self.map.replace('K', '.')
        self.key_obtained = True
        return 'Key Obtained.'

    def unlock_chest(self, output):
        """Unlocks chest and wins the game

        Args:
            output - Converted map. Type(List of Lists of Strings)"""
        self.map = self.revert_map_to_string_state(output)
        self.map = self.map.replace('H', '.')
        self.map = self.map.replace('C', 'H')
        self.unlocked = True
        return 'Chest Unlocked.'

    def battle(self, name, dest, otpt, chr_loc):
        """Invoked when an Entity's destination map block
        is occupied by the opposite entity type

        Args:
            name - Name of the Entity that walks over. Type(String)
            dest - Coordinates of move direction. Type(Tuple)
            otpt - Converted map. Type(List of Lists of Strings)
            chr_loc - Current coordinates of entity. Type(Tuple)"""
        to_fight = None
        for each in self.ingame:
            if self.ingame[each].location == dest:
                to_fight = self.ingame[each]

        battle = Fight(self.ingame[name], to_fight)
        battle_result = battle.simulate_fight()
        otpt[chr_loc[0]][chr_loc[1]] = "."
        otpt[dest[0]][dest[1]] = self.get_player_indicator(battle_result)
        if self.ingame[name] == battle_result:
            self.ingame[name].location = dest
        else:
            self.map = self.map.replace('H', '.')
        for item in self.ingame:
            if self.ingame[item] == battle_result:
                self.map = self.revert_map_to_string_state(otpt)
                return "{} wins!".format(item)

    def move_player(self, player_name, direction):
        """Moves the Player's character to a specified direction

        Args:
            player_name - The name that represents the Hero character
                on the Dungeon map. Type(String). This is decided by the player
            direction - Specified move direction of the Entity. Type(String)"""
        output = self.convert_map_to_changeable_tiles()
        dest = self.get_destination_coordinates(
            self.ingame[player_name].location, direction)

        char_location = self.ingame[player_name].location
        target = output[dest[0]][dest[1]]

        if not self.check_move(target, direction):
            return 'Try again.'

        if target == 'K':
            return self.obtain_key(player_name, dest, output, char_location)
        elif target == 'C':
            if self.key_obtained:
                return self.unlock_chest(output)
            else:
                return 'You must get the key first.'
        elif target == ".":
            return self.regular_move(player_name, dest, output, char_location)
        elif target == 'O':
            return self.battle(player_name, dest, output, char_location)

    def get_random_npc(self):
        """Determine which NPC (if more than one are present) would move"""
        monsters = []
        for each in self.npcs:
            monsters.append(each)
        return monsters[randint(0, len(monsters) - 1)]

    def move_npc(self, npc_name):
        """Attempts to move an NPC into a randomly selected direction

        Args:
            npc_name - Name of spawned NPC to be moved. Type(String)"""
        dirs = ['up', 'down', 'left', 'right']
        direction = dirs[randint(0, len(dirs) - 1)]
        output = self.convert_map_to_changeable_tiles()
        dest = self.get_destination_coordinates(
            self.ingame[npc_name].location, direction)

        char_location = self.ingame[npc_name].location
        target = output[dest[0]][dest[1]]
        if not self.check_move(target, direction):
            return

        if target in ['Z', '#', 'C', 'K', 'O']:
            return
        elif target == '.':
            self.regular_move(npc_name, dest, output, char_location)
        elif target == 'H':
            return self.battle(npc_name, dest, output, char_location)
