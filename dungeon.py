import os
from orc import Orc
from hero import Hero
from weapon import Weapon
from fight import Fight


class Dungeon():

    def __init__(self, map):
        self.map = self.load_map(map)
        self.ingame = {}

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

    def get_position_in_map(self):
        output = self.convert_map_to_changeable_tiles()
        for row in range(0, len(output)):
            for col in range(0, len(output[0])):
                if output[row][col] == 'S':
                    return [row, col]

    def spawn(self, player_name, entity):
        if player_name in self.ingame:
            return 'Character is already spawned.'
        indicator = self.get_player_indicator(entity)
        if 'S' in self.map and indicator:
            self.ingame[player_name] = entity
            entity.location = self.get_position_in_map()
            self.map = (self.map[:self.map.find('S')] + indicator +
                        self.map[self.map.find('S') + 1:])
        else:
            return 'No free spawn slot.'

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

    def check_move(self, direction, destination, output):
        directions = ['left', 'right', 'up', 'down']
        if direction not in directions:
            return "Wrong direction given."

        if (destination[0] < 0 or destination[1] < 0 or
                destination[0] > len(output) or
                destination[1] > len(output[0])):
            return "Out of Bounds."

    def move(self, player_name, direction):
        output = self.convert_map_to_changeable_tiles()
        chr_loc = self.ingame[player_name].location
        dest = self.get_destination_coordinates(
            self.ingame[player_name].location, direction)
        target = output[dest[0]][dest[1]]
        enemy = "OH".replace(
            self.get_player_indicator(self.ingame[player_name]), '')

        self.check_move(direction, dest, output)
        if target == "#":
            return "You will hit the wall."
        elif target == ".":
            self.ingame[player_name].location = dest
            output[chr_loc[0]][chr_loc[1]], output[dest[0]][dest[1]] = output[
                dest[0]][dest[1]], output[chr_loc[0]][chr_loc[1]]
            self.map = self.revert_map_to_string_state(output)
        elif target == enemy:
            to_fight = None
            for each in self.ingame:
                if self.ingame[each].location == dest:
                    to_fight = self.ingame[each]

            battle = Fight(self.ingame[player_name], to_fight)
            battle_result = battle.simulate_fight()
            output[chr_loc[0]][chr_loc[1]] = "."
            output[dest[0]][dest[1]] = self.get_player_indicator(battle_result)
            for item in self.ingame:
                if self.ingame[item] == battle_result:
                    self.map = self.revert_map_to_string_state(output)
                    return "{} wins!".format(item)

# orc = Orc("Orc", 100, 1.4)
# weapon1 = Weapon("Axe", 15, 0.4)
# orc.equip_weapon(weapon1)

# hero = Hero("Hero", 100, "Heroic")
# weapon2 = Weapon("Sword", 14, 0.6)
# hero.equip_weapon(weapon2)

# peshtera = Dungeon("basic_dungeon.txt")
# peshtera.spawn("Player One", orc)
# peshtera.spawn("Player Two", hero)
# peshtera.move("Player One", "right")
# peshtera.move("Player One", "down")
# peshtera.move("Player One", "down")
# peshtera.move("Player One", "down")
# peshtera.move("Player One", "right")
# peshtera.move("Player One", "right")
# peshtera.move("Player One", "right")
# peshtera.move("Player One", "right")
# peshtera.move("Player One", "up")
# peshtera.move("Player Two", "up")
# peshtera.move("Player Two", "up")
# peshtera.move("Player Two", "up")
# peshtera.move("Player Two", "up")
# peshtera.move("Player Two", "left")
# peshtera.move("Player Two", "left")
# peshtera.move("Player Two", "left")
# peshtera.move("Player Two", "left")
# peshtera.move("Player Two", "down")
# print(peshtera.move("Player One", "up"))

# print (peshtera.print_map())
