from weapon import Weapon
from hero import Hero
from dungeon import Dungeon
from random import randint

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
    created = False
    while exit is False:
        full_command = input('--> ').split(' ')
        if full_command[0] == 'load_map':
            dungeon = Dungeon(full_command[1])
        elif full_command[0] == 'show_map':
            print(dungeon.print_map())
        elif full_command[0] == 'create_hero':
            my_hero = Hero(
                full_command[1], int(full_command[2]), full_command[3])
            my_hero.weapon = Weapon('Ashbringer', 40, 0.8)
            created = True
        elif full_command[0] == 'spawn_hero':
            if created is True:
                dungeon.spawn(full_command[1], my_hero)
                dungeon.spawn_npcs()
            else:
                return 'No created characters.'
        elif full_command[0] == 'move':
            if not dungeon.ingame[full_command[1]].is_alive():
                exit = True
                return 'Your character is dead. Game over.'
            else:
                if dungeon.unlocked:
                    exit = True
                    return 'Game Over. You have won.'
                print(dungeon.move_player(full_command[1], full_command[2]))
                to_move = dungeon.get_random_npc()
                if not dungeon.ingame[to_move].is_alive():
                    dungeon.ingame = {
                        i: dungeon.ingame[i] for i in dungeon.ingame if i != 0}
                    dungeon.npcs = {i: dungeon.npcs[i]
                                    for i in dungeon.npcs if i != 0}
                else:
                    print(dungeon.move_npc(to_move))
                print(dungeon.print_map())
        elif full_command[0] == 'heal':
            my_hero.health = my_hero.max_health
        elif full_command[0] == 'help':
            print(helper)
        elif full_command[0] == 'exit':
            exit = True
        else:
            print("Invalid command. Type 'help' for available commands.")

print(start())
