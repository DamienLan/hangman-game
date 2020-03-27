"""
Define the Game class
"""

import random as rd

import modules.word as w


def word_from_database(path):
    """
    Chose a word in the database. If there is no database, return the string error :)
    :param path:
    :return: string
    """
    try:
        with open(path, 'r') as file:
            text = file.read()
            word_list = text.split('\n')
            ind = rd.randrange(len(word_list))

            string = word_list[ind].upper()

            return string
    except FileNotFoundError:
        return 'ERROR'


class Game:
    """
    Game class
    """

    def __init__(self, level):
        """
        init function
        """

        if level == 'hard':
            self.number_of_live = 4
        elif level == 'medium':
            self.number_of_live = 6
        else:
            self.number_of_live = 8

        string = word_from_database('data/word_database.txt')
        self.word = w.Word(string)
        self.answer = string

        self.in_process = True
        self.letter_found = []

    def display(self):
        """
        Display the current situation of the game
        :return: None
        """
        word_disp = self.word.display()

        letter_found_disp = ""
        for letter in self.letter_found:
            letter_found_disp += letter + " "

        print(word_disp)
        print(letter_found_disp)
        print(f'Il te reste {self.number_of_live} vie(s).\n')

    def upgrade(self, char):
        """
        Check if the game is still in process and upgrade the situation
        :param: char
        :return: None
        """
        if char in self.answer:
            self.word.upgrade(char)
        else:
            self.letter_found.append(char.upper())
            self.number_of_live -= 1

        # End of the game
        if self.word.found or self.number_of_live == 0:
            self.in_process = False

    def display_answer(self):
        """
        Display the word of the game
        :return: string
        """
        answer = self.answer.replace("", " ").center(30)

        print(answer)
