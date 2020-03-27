"""
Define the class letter
"""


class Letter:
    """
    Letter class
    """

    def __init__(self, char):
        """
        init function
        :param char: character of the letter
        """
        self.char = char
        self.founded = False

    def reveal(self, char):
        """
        reveal the letter if it is the character given
        :param char:
        :return None
        """
        if self.char == char:
            self.founded = True

    def display(self):
        """
        display the letter
        :return: the letter if it's founded and otherwise '_'
        """
        if self.founded:
            return self.char
        return '_'
