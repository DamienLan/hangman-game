"""
Define the Game class
"""

import random as rd
import word as w


class Game:
    """
    Game class
    """

    def __init__(self, level):
        """
        init function
        """
        with open('data/word_database.txt', 'r') as file:
            text = file.read()
            word_list = text.split('\n')
            ind = rd.randrange(len(word_list))

            string = word_list[ind].upper()

        if level == 'hard':
            self.number_of_live = 4
        elif level == 'medium':
            self.number_of_live = 6
        else:
            self.number_of_live = 8

        self.answer = string
        self.in_process = True
        self.won = False
        self.word = w.Word(string)
        self.letter_founded = []


    def display(self):
        """
        Display the current situation of the game
        :return: None
        """
        word_disp = self.word.display()
        letter_founded_disp = ""

        for letter in self.letter_founded:
            letter_founded_disp += letter + " "

        print(word_disp)
        print(letter_founded_disp)
        print(f'Il te reste {self.number_of_live} vie(s).\n')

    def upgrade(self, char):
        """
        Check if the game is still in process and upgrade the situation
        :param: char
        :return: None
        """
        if char not in self.answer:
            self.letter_founded.append(char.upper())
            self.number_of_live -= 1
        self.word.upgrade(char)

        # End of the game
        if self.word.founded:
            self.in_process = False
            self.won = True
        elif self.number_of_live == 0:
            self.in_process = False
            self.won = False

    def display_answer(self):
        """
        Display the word of the game
        :return: string
        """
        disp = ""
        for char in self.answer:
            disp += char + " "

        disp = disp.center(30)

        print(disp)
