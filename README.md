To start the game, start the 'UI.py' file with the python interpreter.
You can load the 'basic_dungeon.txt' file, or use it as a template to create your own map.


# Available commands:

load_map <Mapfile> - Creates new dungeon with the map in mapfile <br/>
show_map - Displays current dungeon map <br/>
create_hero <Name> <Health> <Nickname> - Creates hero with entered attributes <br/>
spawn_hero <Username> - Spawns hero with specified username into the dungeon <br/>
known_as - Displays name and nickname of hero <br/>
move <Username> <Direction> - Moves the hero in the specified direction <br/>
help - Displays this message <br/>
exit - Closes the program <br/>

# Correct command sequence: 

| load_map <br/>
| show_map <br/>
| create_hero <br/>
| spawn_hero <br/>
V move

The other commands are available throughout the whole game.




# Map legend:

Z - Map bound <br/>
\# - Wall <br/>
. - Free spot <br/>
S - Player spawn point <br/>
N - NPC spawn point <br/>
H - Spawned hero <br/>
O - Spawned NPC(Orc) <br/>
K - Key for treasure chest <br/>
C - Treasure chest <br/>


####To complete the game you must obtain the key and then go unlock the chest. Beware of orcs!