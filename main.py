"""
Main program for the "Jeu du Pendu"
"""
import argparse
import re

import modules.game as g


def parse_arguments():
    """parse argument function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--level")
    return parser.parse_args()


def ask_new_letter():
    """
    Ask a new letter at the player
    :return: charactere chosen
    """
    condition = False
    while not condition:
        char = input("Nouvelle lettre :\n").upper()
        if re.match('[A-Z]$', char):
            condition = True
        else:
            print("Charactère invalide...")
    return char


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
        char = ask_new_letter()
        game.upgrade(char)

    if game.word.found:
        print("Félicitations !! Tu as trouvé :")
        game.display_answer()
    else:
        print("C'est perdu... La réponse était :")
        game.display_answer()


if __name__ == "__main__":
    main()
