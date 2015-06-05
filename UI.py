from weapon import Weapon
from hero import Hero
from orc import Orc
from fight import Fight
from dungeon import Dungeon


helper = """load_map <mapfile.txt> - Creates new dungeon with the map in mapfile
show_map - Displays current dungeon map
create_hero <Name> <Health> <Nickname> - Creates hero with entered attributes
spawn_hero <Username> - Spawns hero with specified username into the dungeon
move <username> <direction> - Moves the hero in the specified direction
help - Displays this message
exit - Closes the program"""


def start():
    print("Welcome. Type 'help' for available commands")
    exit = False
    while exit is False:
        full_command = input('--> ').split(' ')
        if full_command[0] == 'load_map':
            dungeon = Dungeon('basic_dungeon.txt')
        elif full_command[0] == 'show_map':
            print(dungeon.print_map())
        elif full_command[0] == 'create_hero':
            my_hero = Hero(full_command[1], full_command[2], full_command[3])
        elif full_command[0] == 'spawn_hero':
            if not my_hero:
                return 'There is nobody to spawn.'
            dungeon.spawn(full_command[1], my_hero)
            NPC = Orc('Thrall', 400, 1.7)
            dungeon.spawn('NPC1', NPC)
        elif full_command[0] == 'move':
            if not dungeon.ingame[full_command[1]].is_alive():
                return 'Your character has died. Please go away.'
            else:
                dungeon.move(full_command[1], full_command[2])
        elif full_command[0] == 'help':
            print(helper)
        elif full_command[0] == 'exit':
            exit = True
        else:
            print("Invalid command. Type 'help' for available commands.")

start()
