import dice
import sys
import getopt
import systems


def roll_attributes(attribute_array, roll_method):
    attribute_block = {}
    for attribute in attribute_array:
        attribute_block[attribute] = roll_method()
    return attribute_block


# print(SYSTEM.keys())


def main(args):
    """Main function"""
    game_system = "s"
    # file_suffix = "f"

    try:
        opts, args = getopt.getopt(args, "s:", ["system="])
    except getopt.GetoptError:
        print('dcc.py -s <game system>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-s", "--sys"):
            game_system = arg

    print(
        roll_attributes(systems.RPG[game_system]['attributes'],
                        dice.mighty_roll))


if __name__ == '__main__':
    main(sys.argv[1:])
