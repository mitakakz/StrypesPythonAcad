
class Hero :

    def __init__(self, name, title, health, mana, mana_regeneration_rate):

        self.name = name
        self.title = title
        self.health = health
        self.max_health = health
        self.mana = mana
        self.max_mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.posx = 0
        self.posy = 0

    def known_as (self):
        return "{} the {}".format(self.name, self.title)

    def is_alive(self):
        return self.health>0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def can_cast(self):
        return self.mana > 0

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0

    def take_healing(self, healing_points):

        if self.health == 0:
            return False
        self.health += healing_points
        if self.health > self.max_health:
            self.health = self.max_health
        return True

    def take_mana (self, mana_points):

        self.mana += mana_points
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        if self.mana < 0:
            self.mana = 0

    def make_a_move (self):
        self.take_mana(self.mana_regeneration_rate)

    def equip(self, wepon):
        pass

    def learn(self, spell):
        pass

    def attack(self, by):
        pass


class Enemy :

    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage
        self.weapon = None
        self.cast = None

    def is_alive(self):
        return self.health > 0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def can_cast(self):
        return self.mana > 0

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0

    def take_healing(self, healing_points):

        if self.health == 0:
            return False
        self.health += healing_points
        if self.health > self.max_health:
            self.health = self.max_health
        return True

    def take_mana(self, mana_points):

        self.mana += mana_points
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        if self.mana < 0:
            self.mana = 0

    def make_a_move(self):
        self.take_mana(self.mana_regeneration_rate)

    def equip(self, wepon):
        self.weapon = wepon


    def learn(self, spell):
        self.cast = spell

    def attack(self, by):
        if by == "weapon":
            self.damage = self.weapon.damage
        elif by == "magic":
            self.damage = self.cast.damage


class Wepon :

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

class Dungeon:

    def __init__(self, map_file):
        with open(map_file) as f:
            content = f.read()
            self.lines = content.split('\n')

    def print_map(self):

        for line in self.lines:
            print (line)
        #print (self.lines)

    def move_hero(self, direction):
        y = 0
        for line in self.lines:
            if 'H' in line:
                x = line.index('H')
                break
            y += 1
        print (x,y)
        if direction == "up":
            if y > 0:
                pass
        elif direction == "down":
            pass
        elif direction == "left":
            pass
        elif direction == "rigth":
            pass

    def spawn(self, hero,map):
        x = 0
        y = 0
        for line in map.lines:
            if 'S' in line:
                y = line.index("S")
                map.lines[x] = map.lines[x].replace('S','H')
                hero.posx = x
                hero.posy = y
                return True
            x += 1
        return False

if __name__ == '__main__':

    hero = Hero("bashmaistora", "na_more", 100,100,2)
    map = Dungeon("Level1.txt")
    map.print_map()

    print("___________________________")
    map.spawn(hero, map)
    map.print_map()
    map.move_hero("up")
