
class Hero :

    def __init__(self, name, title, health, mana, mana_regeneration_rate):

        self.name = name
        self.title = title
        self.health = health
        self.max_health = health
        self.mana = mana
        self.max_mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate

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
        pass

    def learn(self, spell):
        pass

    def attack(self, by):
        pass


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
            lines = content.split('\n')
            print lines