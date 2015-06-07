import os
from orc import Orc
from hero import Hero
from weapon import Weapon
from fight import Fight
from random import randint


class Dungeon():

    def __init__(self, map):
        self.map = self.load_map(map)
        self.ingame = {}
        self.npcs = {}
        self.key_obtained = False
        self.unlocked = False

    def load_map(self, map_file):
        if not os.path.exists(map_file):
            return ''
        with open(map_file, 'r') as f:
            contents = f.read()
        return contents

    def print_map(self):
        if not self.map:
            return 'No valid map loaded.'
        return self.map

    def convert_map_to_changeable_tiles(self):
        new_map = []
        for item in self.map.split():
            new_map.append(list(item))
        return new_map

    def revert_map_to_string_state(self, custom_map):
        string_map = ''
        for item in custom_map:
            for char in item:
                string_map += char
            string_map += '\n'
        return string_map[:-1]

    def get_player_indicator(self, player):
        entities = ['O', 'H']
        if isinstance(player, Orc):
            return entities[0]
        elif isinstance(player, Hero):
            return entities[1]
        else:
            return ''

    def get_position_in_map(self, ind):
        output = self.convert_map_to_changeable_tiles()
        for row in range(0, len(output)):
            for col in range(0, len(output[0])):
                if output[row][col] == ind:
                    return [row, col]

    def spawn(self, player_name, entity):
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
        directions = ['left', 'right', 'up', 'down']
        if direction not in directions:
            print("Wrong direction given.")
            return False
        if target == "#":
            print("You will hit the wall.")
            return False
        if target == 'Z':
            print('Out of bounds.')
            return False
        return True

    def regular_move(self, name, dest, otpt, chr_loc):
        self.ingame[name].location = dest
        otpt[chr_loc[0]][chr_loc[1]], otpt[dest[0]][dest[1]] = otpt[
            dest[0]][dest[1]], otpt[chr_loc[0]][chr_loc[1]]
        self.map = self.revert_map_to_string_state(otpt)
        return 'Successful Move.'

    def obtain_key(self, name, dest, otpt, chr_loc):
        self.key_obtained = True
        self.ingame[name].location = dest
        otpt[chr_loc[0]][chr_loc[1]], otpt[dest[0]][dest[1]] = otpt[
            dest[0]][dest[1]], otpt[chr_loc[0]][chr_loc[1]]
        self.map = self.revert_map_to_string_state(otpt)
        self.map = self.map.replace('K', '.')
        return 'Key Obtained.'

    def unlock_chest(self, output):
        self.map = self.revert_map_to_string_state(output)
        self.map = self.map.replace('H', '.')
        self.map = self.map.replace('C', 'H')
        self.unlocked = True
        return 'Chest Unlocked.'

    def battle(self, name, dest, otpt, chr_loc):
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
        monsters = []
        for each in self.npcs:
            monsters.append(each)
        return monsters[randint(0, len(monsters) - 1)]

    def move_npc(self, npc_name):
        dirs = ['up', 'down', 'left', 'right']
        direction = dirs[randint(0, len(dirs) - 1)]
        output = self.convert_map_to_changeable_tiles()
        dest = self.get_destination_coordinates(
            self.ingame[npc_name].location, direction)

        char_location = self.ingame[npc_name].location
        target = output[dest[0]][dest[1]]
        if not self.check_move(target, direction):
            return

        if (target == 'Z' or target == '#' or target == 'C'
                or target == 'K' or target == 'O'):
            return
        elif target == '.':
            self.regular_move(npc_name, dest, output, char_location)
        elif target == 'H':
            return self.battle(npc_name, dest, output, char_location)
