"""
Main program for the "Jeu du Pendu"
"""
import argparse

import class.game as g


def parse_arguments():
    """parse argument function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--level")
    return parser.parse_args()


def main():
    """
    main function, process the game
    :return: None
    """
    args = parse_arguments()

    game = g.Game(args.level)

    print("Bienvenue !\n")
    while game.in_process:
        game.display()
        condition = False
        while not condition:
            char = input("Nouvelle lettre :\n").upper()
            if isinstance(char, str) and len(char) == 1:
                condition = True
            else:
                print("Charactère invalide...")

        game.upgrade(char)

    if game.won:
        print("Félicitations !! Tu as trouvé :")
        game.display_answer()
    else:
        print("C'est perdu... La réponse était :")
        game.display_answer()


if __name__ == "__main__":
    main()
