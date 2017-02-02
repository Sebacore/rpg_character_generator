import mixin
import dice
import occupations
import random


class PlayerCharacter(mixin.Attributes):
    def __init__(self, rpg_system, dice_method):
        self.attribute_array = rpg_system['attributes']
        self.system = rpg_system['name']
        # self.system = rpg_system['name']
        self.dice_method = dice_method
        self.attributes = self.roll_attributes(self.attribute_array,
                                               self.dice_method, rpg_system)
        self.class_name = self.get_class_name(rpg_system, self.attributes)

        if not self.system == 'Dungeon Crawl Classic':
            self.max_hp = self.get_max_hp(rpg_system, self.class_name,
                                          self.attributes['CON'])
        else:
            self.max_hp = self.get_max_hp(rpg_system, self.class_name,
                                          self.attributes['STA'])
        self.occupation = self.get_occupation()

    def get_max_hp(self, rpg_system, class_name, attribute):
        # TODO: Get system, class and roll hitdice and add relivent modifier.
        # Value can not be less than 1.
        hit_dice = rpg_system['classes'][class_name]['hitdice']
        modifier = attribute['modifier']
        max_hp = dice.die(hit_dice) + modifier
        if max_hp > 0:
            max_hp = 1
        return max_hp

    def get_class_name(self, system, attribute_scores):
        prime_attribute = sorted(self.attributes, reverse=True)[:1]
        if prime_attribute == 'LCK':
            prime_attribute = sorted(self.attributes, reverse=True)[1:2]
        if not self.system == 'Dungeon Crawl Classic':
            for classname, prime in system['prime_attributes'].items():
                if prime == prime_attribute[0]:
                    name_of_class = classname.capitalize()
                    return name_of_class
        else:
            return "Zero"

    def get_occupation(self):
        return random.choice(occupations.occupations)
