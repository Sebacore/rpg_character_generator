import dice
import getopt
import sys
import systems


def main(args):
    """Main function"""
    game_system = "s"
    # file_suffix = "f"

    try:
        opts, args = getopt.getopt(args, "s:", ["system="])
    except getopt.GetoptError:
        print('rpg_character_generator.py -s <game system>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-s", "--sys"):
            game_system = arg

    rpg_game = systems.RPG[game_system]


if __name__ == '__main__':
    main(sys.argv[1:])
