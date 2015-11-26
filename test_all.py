from entity import Entity
from weapon import Weapon
from hero import Hero
from orc import Orc
from fight import Fight
from dungeon import Dungeon
from os import remove
import unittest


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.entity = Entity('Arthas', 200)
        self.entity.weapon = Weapon('Frostmourne', 35, 0.7)

    def test_init(self):
        self.assertEqual(self.entity.name, 'Arthas')
        self.assertEqual(self.entity.health, 200)

    def test_get_health(self):
        self.assertEqual(self.entity.get_health(), 200)

    def test_is_alive_when_alive(self):
        self.assertTrue(self.entity.is_alive())

    def test_is_alive_when_dead(self):
        self.entity.health = 0
        self.assertFalse(self.entity.is_alive())

    def test_take_damage_common(self):
        self.entity.take_damage(150)
        self.assertTrue(self.entity.is_alive())
        self.assertEqual(self.entity.get_health(), 50)

    def test_take_damage_full(self):
        self.entity.take_damage(350)
        self.assertFalse(self.entity.is_alive())
        self.assertEqual(self.entity.get_health(), 0)

    def test_take_healing_common(self):
        self.entity.health = 50
        self.entity.take_healing(50)
        self.assertEqual(self.entity.get_health(), 100)

    def test_take_healing_full(self):
        self.entity.take_healing(350)
        self.assertEqual(self.entity.get_health(), 200)

    def test_take_healing_when_dead(self):
        self.entity.health = 0
        self.entity.take_healing(100)
        self.assertEqual(self.entity.health, 0)

    def test_has_weapon_when_present(self):
        self.assertEqual(self.entity.has_weapon(), True)

    def test_has_weapon_when_not_present(self):
        self.entity.weapon = None
        self.assertEqual(self.entity.has_weapon(), False)

    def test_equip_stronger_weapon(self):
        test_weapon = Weapon('Stick', 500, 0.1)
        self.entity.equip_weapon(test_weapon)
        self.assertEqual(self.entity.weapon, test_weapon)

    def test_equip_weaker_weapon(self):
        test_weapon = Weapon('Stick', 5, 0.1)
        self.entity.equip_weapon(test_weapon)
        self.assertNotEqual(self.entity.weapon, test_weapon)

    def test_equip_weapon_when_not_armed(self):
        test_weapon = Weapon('Stick', 5, 0.1)
        self.entity.weapon = None
        self.entity.equip_weapon(test_weapon)
        self.assertEqual(self.entity.weapon, test_weapon)

    def test_attack_when_no_weapon_is_equipped(self):
        self.entity.weapon = None
        self.assertEqual(self.entity.attack(), 0)

    def test_attack_when_weapon_is_equipped(self):
        self.assertIn(self.entity.attack(), [35, 70])


class TestOrc(unittest.TestCase):

    def setUp(self):
        self.orc = Orc('Thrall', 200, 1.7)
        self.orc.weapon = Weapon('Frostmourne', 35, 0.7)

    def test_init(self):
        self.assertEqual(self.orc.name, 'Thrall')
        self.assertEqual(self.orc.health, 200)
        self.assertEqual(self.orc.berserk_factor, 1.7)

    def test_berserk_set_with_higher_value(self):
        result = self.orc.set_berserk_factor(3.5)
        self.assertEqual(result, 2.0)

    def test_berserk_set_with_lower_value(self):
        result = self.orc.set_berserk_factor(0.4)
        self.assertEqual(result, 1.0)

    def test_berserk_set_with_negative(self):
        result = self.orc.set_berserk_factor(-5)
        self.assertEqual(result, 1.0)

    def test_has_weapon_when_present(self):
        self.assertEqual(self.orc.has_weapon(), True)

    def test_has_weapon_when_not_present(self):
        self.orc.weapon = None
        self.assertEqual(self.orc.has_weapon(), False)

    def test_equip_stronger_weapon(self):
        test_weapon = Weapon('Stick', 500, 0.1)
        self.orc.equip_weapon(test_weapon)
        self.assertEqual(self.orc.weapon, test_weapon)

    def test_equip_weaker_weapon(self):
        test_weapon = Weapon('Stick', 5, 0.1)
        self.orc.equip_weapon(test_weapon)
        self.assertNotEqual(self.orc.weapon, test_weapon)

    def test_attack_when_no_weapon_is_equipped(self):
        self.orc.weapon = None
        self.assertEqual(self.orc.attack(), 0)

    def test_attack_when_weapon_is_equipped(self):
        self.assertIn(self.orc.attack(), [35 * 1.7, 70 * 1.7])


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero = Hero('Arthas', 1000, 'Lich King')
        self.hero.weapon = Weapon('Frostmourne', 35, 0.7)

    def test_init(self):
        self.assertEqual(self.hero.name, 'Arthas')
        self.assertEqual(self.hero.health, 1000)
        self.assertEqual(self.hero.nickname, 'Lich King')

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), 'Arthas the Lich King')

    def test_has_weapon_when_present(self):
        self.assertEqual(self.hero.has_weapon(), True)

    def test_has_weapon_when_not_present(self):
        self.hero.weapon = None
        self.assertEqual(self.hero.has_weapon(), False)

    def test_equip_stronger_weapon(self):
        test_weapon = Weapon('Stick', 500, 0.1)
        self.hero.equip_weapon(test_weapon)
        self.assertEqual(self.hero.weapon, test_weapon)

    def test_equip_weaker_weapon(self):
        test_weapon = Weapon('Stick', 5, 0.1)
        self.hero.equip_weapon(test_weapon)
        self.assertNotEqual(self.hero.weapon, test_weapon)

    def test_attack_when_no_weapon_is_equipped(self):
        self.hero.weapon = None
        self.assertEqual(self.hero.attack(), 0)

    def test_attack_when_weapon_is_equipped(self):
        self.assertIn(self.hero.attack(), [35, 70])


class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.weapon = Weapon('Sword', 11, 0.4)

    def test_init(self):
        self.assertEqual(self.weapon.type, 'Sword')
        self.assertEqual(self.weapon.damage, 11)
        self.assertEqual(self.weapon.critical_percent, 0.4)

    def test_set_crit_with_higher_value(self):
        result = self.weapon.set_critical_percent(3)
        self.assertEqual(result, 1.0)

    def test_set_crit_witn_lower_value(self):
        result = self.weapon.set_critical_percent(-1)
        self.assertEqual(result, 0.1)

    def test_critical_strike_chance(self):
        self.assertIn(self.weapon.critical_hit(), [True, False])


class TestFight(unittest.TestCase):

    def setUp(self):
        self.hero = Hero('Arthas', 660, 'Lich King')
        self.orc = Orc('Thrall', 700, 1.7)
        self.heroWeapon = Weapon('Frostmourne', 35, 0.7)
        self.orcWeapon = Weapon('Doomhammer', 40, 0.6)
        self.hero.weapon = self.heroWeapon
        self.orc.weapon = self.orcWeapon
        self.fight = Fight(self.hero, self.orc)

    def test_init(self):
        self.assertEqual(self.fight.hero, self.hero)
        self.assertEqual(self.fight.orc, self.orc)

    def test_coin_toss_for_first_attacker(self):
        self.assertIn(self.fight.coin_toss(),
                      [(self.orc, self.hero), (self.hero, self.orc)])

    def test_simulate_fight_with_no_weapons(self):
        self.fight.hero.weapon = None
        self.fight.orc.weapon = None
        result = self.fight.simulate_fight()
        self.assertEqual(result, 'No winner')

    def test_simulate_fight_with_only_one_weapon(self):
        self.fight.hero.weapon = None
        result = self.fight.simulate_fight()
        self.assertEqual(result, self.fight.orc)

    def test_simulate_fight_with_both_armed_chars(self):
        result = self.fight.simulate_fight()
        self.assertIn(result, [self.fight.orc, self.hero])


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.mapfile = 'testmap.txt'
        self.mapcontents = """ZZZZZZZZZZZZZZZZZZZ\nZ#...#.##.########Z
Z#.S.#.....N....K.Z\nZ#...#..#.....####Z
Z#...#..#.....N..#Z\nZ....#..#......#.#Z
Z#......#..N...#.#Z\nZ..............#C#Z
Z..###########....Z\nZZZZZZZZZZZZZZZZZZZ"""
        with open(self.mapfile, "w+") as f:
            f.write(self.mapcontents)

        self.dungeon = Dungeon('testmap.txt')
        self.hero = Hero('Arthas', 500, 'Lich King')
        self.orc = Orc('Thrall', 500, 1.6)

    def tearDown(self):
        remove(self.mapfile)

    def test_init(self):
        self.assertEqual(self.dungeon.map, self.mapcontents)

    def test_load_map_with_valid_file(self):
        result = self.dungeon.load_map('testmap.txt')
        self.assertEqual(result, self.mapcontents)

    def test_load_map_with_invalid_file(self):
        result = self.dungeon.load_map('not_exists.txt')
        self.assertEqual(result, '')

    def test_map_with_empty_file(self):
        with open(self.mapfile, 'w') as f:
            f.write('')

        result = self.dungeon.load_map('testmap.txt')
        self.assertEqual(result, '')

    def test_print_map_with_valid_file(self):
        result = self.dungeon.print_map()
        self.assertEqual(result, self.mapcontents)

    def test_print_map_with_empty_file(self):
        self.dungeon.map = ''
        result = self.dungeon.print_map()
        self.assertEqual(result, 'No valid map loaded.')

    def test_print_map_after_battle(self):
        hero = Hero("Alan", 1, "Turing")
        hero.weapon = Weapon("Stick", 1, 0.1)
        self.dungeon.map = "ZSNZ"
        self.dungeon.spawn("1", hero)
        self.dungeon.spawn_npcs()

        self.dungeon.move_player("1", "right")
        self.assertEqual(self.dungeon.map, "Z.OZ")

    def test_valid_spawn(self):
        self.dungeon.spawn('Player 1', self.hero)
        contents = """ZZZZZZZZZZZZZZZZZZZ\nZ#...#.##.########Z
Z#.H.#.....N....K.Z\nZ#...#..#.....####Z
Z#...#..#.....N..#Z\nZ....#..#......#.#Z
Z#......#..N...#.#Z\nZ..............#C#Z
Z..###########....Z\nZZZZZZZZZZZZZZZZZZZ"""
        self.assertEqual(self.dungeon.map, contents)

    def test_spawn_when_char_is_ingame(self):
        self.dungeon.spawn('Player 1', self.hero)
        result = self.dungeon.spawn('Player 1', self.hero)
        self.assertEqual(result, 'Character is already spawned.')

    def test_spawn_when_no_free_slots(self):
        self.dungeon.spawn('Player 1', self.hero)
        self.dungeon.spawn('Player 2', self.orc)
        testchar = Hero('Arthas', 200, 'Lich')
        result = self.dungeon.spawn('Player 3', testchar)
        self.assertEqual(result, 'No free spawn slot.')

    def test_map_conversion(self):
        actual = [['Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z',
                   'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z'],
                  ['Z', '#', '.', '.', '.', '#', '.', '#', '#', '.', '#', '#',
                   '#', '#', '#', '#', '#', '#', 'Z'],
                  ['Z', '#', '.', 'S', '.', '#', '.', '.', '.', '.', '.', 'N',
                   '.', '.', '.', '.', 'K', '.', 'Z'],
                  ['Z', '#', '.', '.', '.', '#', '.', '.', '#', '.', '.', '.',
                   '.', '.', '#', '#', '#', '#', 'Z'],
                  ['Z', '#', '.', '.', '.', '#', '.', '.', '#', '.', '.', '.',
                   '.', '.', 'N', '.', '.', '#', 'Z'],
                  ['Z', '.', '.', '.', '.', '#', '.', '.', '#', '.', '.', '.',
                  '.', '.', '.', '#', '.', '#', 'Z'],
                  ['Z', '#', '.', '.', '.', '.', '.', '.', '#', '.', '.', 'N',
                   '.', '.', '.', '#', '.', '#', 'Z'],
                  ['Z', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                   '.', '.', '.', '#', 'C', '#', 'Z'],
                  ['Z', '.', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#',
                   '#', '#', '.', '.', '.', '.', 'Z'],
                  ['Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z',
                   'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z']]
        result = self.dungeon.convert_map_to_changeable_tiles()
        self.assertEqual(result, actual)

    def test_map_revert(self):
        test = self.dungeon.convert_map_to_changeable_tiles()
        result = self.dungeon.revert_map_to_string_state(test)
        self.assertEqual(result, self.dungeon.map)

    def test_locate_position(self):
        result = self.dungeon.get_position_in_map('S')
        self.assertEqual(result, [2, 3])

    def test_destination_coordinates_down(self):
        result = self.dungeon.get_destination_coordinates([4, 4], 'down')
        self.assertEqual(result, [5, 4])

    def test_destination_coordinates_up(self):
        result = self.dungeon.get_destination_coordinates([4, 4], 'up')
        self.assertEqual(result, [3, 4])

    def test_destination_coordinates_left(self):
        result = self.dungeon.get_destination_coordinates([4, 4], 'left')
        self.assertEqual(result, [4, 3])

    def test_destination_coordinates_right(self):
        result = self.dungeon.get_destination_coordinates([4, 4], 'right')
        self.assertEqual(result, [4, 5])

    def test_check_move_with_wrong_direction(self):
        result = self.dungeon.check_move('.', 'test')
        self.assertEqual(result, False)

    def test_check_move_with_out_of_bounds_err(self):
        result = self.dungeon.check_move('Z', 'up')
        self.assertEqual(result, False)

    def test_check_move_into_wall(self):
        result = self.dungeon.check_move('#', 'left')
        self.assertEqual(result, False)

    def test_valid_move_into_free_space(self):
        self.dungeon.spawn('1', self.hero)
        self.dungeon.move_player('1', 'right')
        self.assertEqual(self.hero.location, [2, 4])

    def test_invalid_hero_move(self):
        self.dungeon.map = "ZZZ\nZSZ\nZZZ"
        self.dungeon.spawn('Char', self.hero)
        result = self.dungeon.move_player("Char", "left")
        self.assertEqual(result, "Try again.")

    def test_move_npc_into_border(self):
        self.dungeon.map = "ZZZ\nZNZ\nZZZ"
        self.dungeon.spawn_npcs()
        result = self.dungeon.move_npc('NPC1')
        self.assertEqual(result, None)

    def test_move_npc_into_key(self):
        self.dungeon.map = "KKK\nKNK\nKKK"
        self.dungeon.spawn_npcs()
        result = self.dungeon.move_npc('NPC1')
        self.assertEqual(result, None)

    def test_move_npc_into_chest(self):
        self.dungeon.map = "CCC\nCNC\nCCC"
        self.dungeon.spawn_npcs()
        result = self.dungeon.move_npc('NPC1')
        self.assertEqual(result, None)

    def test_move_npc_into_wall(self):
        self.dungeon.map = "###\n#N#\n###"
        self.dungeon.spawn_npcs()
        result = self.dungeon.move_npc('NPC1')
        self.assertEqual(result, None)

    def test_move_npc_into_orc(self):
        self.dungeon.map = "OOO\nONO\nOOO"
        self.dungeon.spawn_npcs()
        result = self.dungeon.move_npc('NPC1')
        self.assertEqual(result, None)

    def test_move_hero_into_battle(self):
        mod = "ZZZZ\nZSNZ\nZZZZ"
        self.dungeon.map = mod
        self.dungeon.spawn('1', self.hero)
        self.dungeon.spawn_npcs()
        self.hero.weapon = Weapon('Frostmourne', 40, 0.9)
        result = self.dungeon.move_player('1', 'right')
        self.assertIn(result, ['1 wins!', 'NPC1 wins!'])

    def test_move_npc_into_battle(self):
        mod = "ZZSZ\nZSNS\nZZSZ"
        self.dungeon.map = mod
        self.dungeon.spawn('1', self.hero)
        self.dungeon.spawn('2', Hero("Tirion", 1, "Fondring"))
        self.dungeon.spawn('3', Hero("Lich", 1, "King"))
        self.dungeon.spawn('4', Hero("Bat", 1, "Svetlio"))
        self.dungeon.spawn_npcs()

        result = self.dungeon.move_npc("NPC1")
        self.assertIn(result, ['1 wins!', 'NPC1 wins!'])

    def test_spawn_npcs(self):
        mod = "ZZZZ\nZN.Z\nZ.NZ\nZZZZ"
        self.dungeon.map = mod
        self.dungeon.spawn_npcs()
        actual = "ZZZZ\nZO.Z\nZ.OZ\nZZZZ"
        self.assertEqual(self.dungeon.map, actual)

    def test_obtain_key(self):
        mod = "ZZZZ\nZS.Z\nZK.Z\nZZZZ"
        self.dungeon.map = mod
        self.dungeon.spawn('1', self.hero)
        result = self.dungeon.move_player('1', 'down')
        self.assertEqual(result, 'Key Obtained.')

    def test_unlock_chest_when_key_is_obtained(self):
        mod = "ZZZZ\nZSKZ\nZ.CZ\nZZZZ"
        self.dungeon.map = mod
        self.dungeon.spawn('1', self.hero)
        self.dungeon.move_player('1', 'right')
        result = self.dungeon.move_player('1', 'down')
        self.assertEqual(result, 'Chest Unlocked.')

    def test_unlock_chest_when_key_not_present(self):
        mod = "ZZZZ\nZS.Z\nZC.Z\nZZZZ"
        self.dungeon.map = mod
        self.dungeon.spawn('1', self.hero)
        result = self.dungeon.move_player('1', 'down')
        self.assertEqual(result, 'You must get the key first.')

    def test_get_random_npc(self):
        mod = "ZZZZ\nZNNZ\nZCNZ\nZZZZ"
        self.dungeon.map = mod
        self.dungeon.spawn_npcs()
        result = self.dungeon.get_random_npc()
        self.assertIn(result, self.dungeon.npcs)

    def test_move_npc_to_empty_spot(self):
        mod = "ZZZZZZZ\nZ.....Z\nZ..N..Z\nZ.....Z\nZZZZZZZ"
        self.dungeon.map = mod
        self.dungeon.spawn_npcs()
        self.dungeon.move_npc(self.dungeon.get_random_npc())
        self.assertIn(self.dungeon.map, [
            "ZZZZZZZ\nZ..O..Z\nZ.....Z\nZ.....Z\nZZZZZZZ",
            "ZZZZZZZ\nZ.....Z\nZ.O...Z\nZ.....Z\nZZZZZZZ",
            "ZZZZZZZ\nZ.....Z\nZ...O.Z\nZ.....Z\nZZZZZZZ",
            "ZZZZZZZ\nZ.....Z\nZ.....Z\nZ..O..Z\nZZZZZZZ"])

    def test_move_to_invalid_spot(self):
        mod = "ZZZZZZZ\nZ..K..Z\nZ.#NC.Z\nZ..O..Z\nZZZZZZZ"
        self.dungeon.map = mod
        self.dungeon.spawn_npcs()
        self.dungeon.move_npc(self.dungeon.get_random_npc())
        self.assertEqual(self.dungeon.map, mod.replace('N', 'O'))

    def test_get_invalid_indicator(self):
        self.invalid = Entity("Name", 20)
        self.assertEqual(self.dungeon.get_entity_indicator(self.invalid), "")

if __name__ == '__main__':
    unittest.main()
