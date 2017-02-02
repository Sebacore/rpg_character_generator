class Attributes(object):
    """
    Generate attritubes for RPG character based on game system.
    Scores are produced using the selected roll method.
    """

    def __init__(self, game_system, roll_method):
        self.attributes = self.roll_attributes(game_system['attributes'],
                                               roll_method, game_system)

    def roll_attributes(self, attribute_array, roll_method, game_system):
        """Return block of attributes based on game system selected."""
        attribute_block = {}
        for attribute in attribute_array:
            score = roll_method()
            attribute_block[attribute] = {
                'score': score,
                'modifier': self.get_bonues(attribute, score,
                                            game_system['modifiers'])
            }

        return attribute_block

    def get_bonues(self, attr, val, modifier_list):
        """Get game system attribute modifers."""
        if val in modifier_list:
            bonus = modifier_list[val]
        return bonus
