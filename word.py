"""
Define the word class
"""
import letter as l


class Word:
    """
    Word class
    """

    def __init__(self, string):
        """
        init function
        :param string: word chosen
        """
        letter_list = []
        for char in string:
            letter_list.append(l.Letter(char))
        self.letter_list = letter_list

        self.founded = False

    def reveal(self, char):
        """
        reveal all the letter if the character given is in the word using reveal letter method
        :param char: character given by user
        :return: None
        """
        for letter in self.letter_list:
            letter.reveal(char)

    def upgrade(self, char):
        """
        Check if the word is founded
        :param char: character given by user
        :return: None
        """
        self.reveal(char)

        for letter in self.letter_list:
            if not letter.founded:
                return None
        self.founded = True

    def display(self):
        """
        Display the word with reveal and not reveal letter
        :return: string
        """
        disp = ""
        for letter in self.letter_list:
            disp += letter.display() + " "

        disp = disp.center(30)

        return disp
