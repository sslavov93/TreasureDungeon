# TODO:
# Add map display after move method execution
# Cover 100% of the classes
# Add docstrings
# Dungeon.py - move npc - if target in...
# Remove useless string returns

from weapon import Weapon
from hero import Hero
from dungeon import Dungeon


class UserInterface():

    def __init__(self):
        self.command_list = {
            "load_map": self.load_map,
            "show_map": self.display_map,
            "create_hero": self.create_character,
            "known_as": self.known_as,
            "spawn_hero": self.spawn_character,
            "move": self.move_character,
            "heal": self.heal_character,
            "help": self.help_message,
            "exit": self.exit_game
        }
        self.exit = False
        self.is_created = False
        self.map_loaded = False
        self.input = None
        self.help = """load_map <mapfile.txt> - Creates new dungeon with the map in mapfile
show_map - Displays current dungeon map
create_hero <Name> <Health> <Nickname> - Creates hero with entered attributes
spawn_hero <Username> - Spawns hero with specified username into the dungeon
known_as - Displays name and nickname of hero
move <username> <direction> - Moves the hero in the specified direction
help - Displays this message
exit - Closes the program"""

    def start_game(self):
        print("Welcome. Type 'help' for available commands")
        while self.exit is False:
            command = self.get_input_command()
            if command[0] in self.command_list:
                execute = self.command_list[command[0]]
                output = execute()
                print(output) if output is not None else None
            else:
                print("Invalid command. Type 'help' for available commands.")

    def get_input_command(self):
        self.input = input('--> ').strip().split(' ')
        return self.input

    def load_map(self):
        self.dungeon = Dungeon(self.input[1])
        if self.dungeon.map:
            self.map_loaded = True

    def display_map(self):
        return self.dungeon.print_map()

    def create_character(self):
        self.char = Hero(self.input[1], int(self.input[2]), self.input[3])
        self.char.weapon = Weapon('Ashbringer', 40, 0.8)
        self.is_created = True

    def known_as(self):
        return self.char.known_as()

    def spawn_character(self):
        if self.is_created is True:
            self.dungeon.spawn(self.input[1], self.char)
            self.dungeon.spawn_npcs()
        else:
            return 'No created characters.'

    def move_character(self):
        if self.input[1] not in self.dungeon.ingame:
            return 'Player name is incorrect.'

        elif not self.dungeon.ingame[self.input[1]].is_alive():
            self.exit = True
            return 'Your character is dead. Game over.'
        else:
            if self.dungeon.unlocked:
                self.exit = True
                return 'Game Over. You have won.'
            return self.dungeon.move_player(self.input[1], self.input[2])
            to_move = self.dungeon.get_random_npc()
            if not self.dungeon.ingame[to_move].is_alive():
                self.dungeon.ingame = {i: self.dungeon.ingame[i]
                                       for i in self.dungeon.ingame
                                       if i != 0}
                self.dungeon.npcs = {i: self.dungeon.npcs[i]
                                     for i in self.dungeon.npcs if i != 0}
            else:
                return self.dungeon.move_npc(to_move)
            return self.display_map()

    def heal_character(self):
        if self.is_created and self.map_loaded:
            self.char.health = self.char.max_health
        else:
            return 'No created characters.'

    def help_message(self):
        return self.help

    def exit_game(self):
        self.exit = True
        return "Goodbye!"


game = UserInterface()
game.start_game()
